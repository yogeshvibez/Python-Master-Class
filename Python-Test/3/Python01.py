#!/usr/bin/env python3
"""
Advanced Joke Generator with Text-to-Speech
A comprehensive Python application that generates jokes with audio output,
featuring configuration management, logging, CLI interface, and extensibility.
"""

import os
import sys
import time
import json
import logging
import argparse
import subprocess
import platform
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import threading
import queue
import signal
import atexit

# Third-party imports with graceful fallbacks
try:
    import pyjokes
    PYJOKES_AVAILABLE = True
except ImportError:
    PYJOKES_AVAILABLE = False
    print("Warning: pyjokes not available. Install with: pip install pyjokes")

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("Warning: gTTS not available. Install with: pip install gtts")

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("Warning: pygame not available for advanced audio. Install with: pip install pygame")

# Configuration
@dataclass
class Config:
    """Configuration settings for the joke generator"""
    joke_count: int = 10
    delay_seconds: float = 3.0
    language: str = "en"
    audio_enabled: bool = True
    save_audio: bool = True
    audio_format: str = "mp3"
    log_level: str = "INFO"
    max_file_size_mb: int = 100
    backup_count: int = 5
    categories: List[str] = None
    output_dir: str = "jokes_output"
    config_file: str = "joke_config.json"
    
    def __post_init__(self):
        if self.categories is None:
            self.categories = ["neutral", "chuck", "all"]

class JokeLogger:
    """Custom logger with rotation and multiple handlers"""
    
    def __init__(self, name: str, log_level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # Create logs directory
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # File handler with rotation
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler(
            log_dir / "joke_generator.log",
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level.upper()))
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def get_logger(self):
        return self.logger

class AudioManager:
    """Manages audio playback with cross-platform support"""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = JokeLogger("AudioManager").get_logger()
        self.audio_queue = queue.Queue()
        self.playback_thread = None
        self.stop_event = threading.Event()
        
    def text_to_speech(self, text: str, filename: str = None) -> Optional[str]:
        """Convert text to speech and save audio file"""
        if not GTTS_AVAILABLE:
            self.logger.warning("gTTS not available, skipping audio generation")
            return None
            
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"joke_{timestamp}.{self.config.audio_format}"
            
            filepath = Path(self.config.output_dir) / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            tts = gTTS(text=text, lang=self.config.language, slow=False)
            tts.save(str(filepath))
            
            self.logger.info(f"Audio saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            self.logger.error(f"Error generating audio: {e}")
            return None
    
    def play_audio(self, filepath: str) -> bool:
        """Play audio file with cross-platform support"""
        try:
            if not os.path.exists(filepath):
                self.logger.error(f"Audio file not found: {filepath}")
                return False
            
            system = platform.system()
            
            if system == "Windows":
                os.startfile(filepath)
            elif system == "Darwin":  # macOS
                subprocess.run(["afplay", filepath])
            elif system == "Linux":
                subprocess.run(["mpg123", filepath])
            else:
                self.logger.warning(f"Unsupported platform: {system}")
                return False
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error playing audio: {e}")
            return False
    
    def start_background_playback(self):
        """Start background audio playback thread"""
        def playback_worker():
            while not self.stop_event.is_set():
                try:
                    filepath = self.audio_queue.get(timeout=1)
                    if filepath:
                        self.play_audio(filepath)
                        self.audio_queue.task_done()
                except queue.Empty:
                    continue
        
        self.playback_thread = threading.Thread(target=playback_worker, daemon=True)
        self.playback_thread.start()
    
    def stop_background_playback(self):
        """Stop background audio playback"""
        self.stop_event.set()
        if self.playback_thread:
            self.playback_thread.join(timeout=2)

class JokeManager:
    """Manages joke generation, storage, and retrieval"""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = JokeLogger("JokeManager").get_logger()
        self.jokes_history = []
        self.audio_manager = AudioManager(config)
        
    def install_dependencies(self):
        """Install required dependencies"""
        dependencies = ["pyjokes", "gtts"]
        
        for dep in dependencies:
            try:
                __import__(dep)
                self.logger.info(f"{dep} already installed")
            except ImportError:
                self.logger.info(f"Installing {dep}...")
                subprocess.run([sys.executable, "-m", "pip", "install", dep])
    
    def get_joke(self, category: str = None) -> Dict[str, Any]:
        """Get a joke with metadata"""
        if not PYJOKES_AVAILABLE:
            return {
                "text": "Why don't scientists trust atoms? Because they make up everything!",
                "category": "fallback",
                "timestamp": datetime.now().isoformat()
            }
        
        try:
            if category and category in self.config.categories:
                joke_text = pyjokes.get_joke(category=category)
            else:
                joke_text = pyjokes.get_joke()
            
            joke_data = {
                "text": joke_text,
                "category": category or "general",
                "timestamp": datetime.now().isoformat(),
                "id": len(self.jokes_history) + 1
            }
            
            self.jokes_history.append(joke_data)
            return joke_data
            
        except Exception as e:
            self.logger.error(f"Error getting joke: {e}")
            return {
                "text": "Error getting joke. Please try again.",
                "category": "error",
                "timestamp": datetime.now().isoformat()
            }
    
    def save_jokes_history(self):
        """Save jokes history to JSON file"""
        try:
            output_dir = Path(self.config.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            history_file = output_dir / "jokes_history.json"
            with open(history_file, 'w') as f:
                json.dump(self.jokes_history, f, indent=2)
                
            self.logger.info(f"Jokes history saved to {history_file}")
            
        except Exception as e:
            self.logger.error(f"Error saving jokes history: {e}")
    
    def load_jokes_history(self):
        """Load jokes history from JSON file"""
        try:
            history_file = Path(self.config.output_dir) / "jokes_history.json"
            if history_file.exists():
                with open(history_file, 'r') as f:
                    self.jokes_history = json.load(f)
                self.logger.info(f"Loaded {len(self.jokes_history)} jokes from history")
                
        except Exception as e:
            self.logger.error(f"Error loading jokes history: {e}")

class JokeGeneratorApp:
    """Main application class"""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = JokeLogger("JokeGeneratorApp").get_logger()
        self.joke_manager = JokeManager(config)
        self.running = False
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        # Cleanup on exit
        atexit.register(self.cleanup)
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.logger.info(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def cleanup(self):
        """Cleanup resources on exit"""
        self.logger.info("Cleaning up resources...")
        self.joke_manager.audio_manager.stop_background_playback()
        self.joke_manager.save_jokes_history()
    
    def load_config(self):
        """Load configuration from file"""
        try:
            config_file = Path(self.config.config_file)
            if config_file.exists():
                with open(config_file, 'r') as f:
                    config_data = json.load(f)
                    for key, value in config_data.items():
                        if hasattr(self.config, key):
                            setattr(self.config, key, value)
                self.logger.info("Configuration loaded from file")
                
        except Exception as e:
            self.logger.error(f"Error loading config: {e}")
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config.config_file, 'w') as f:
                json.dump(asdict(self.config), f, indent=2)
            self.logger.info("Configuration saved to file")
            
        except Exception as e:
            self.logger.error(f"Error saving config: {e}")
    
    def run_interactive(self):
        """Run in interactive mode"""
        self.logger.info("Starting interactive mode")
        self.running = True
        
        print("\n" + "="*50)
        print("🎭 Advanced Joke Generator")
        print("="*50)
        print("Commands:")
        print("  j - Get a joke")
        print("  s - Save history")
        print("  h - Show history")
        print("  c - Show config")
        print("  q - Quit")
        print("="*50 + "\n")
        
        while self.running:
            try:
                command = input("Enter command: ").strip().lower()
                
                if command == 'j':
                    joke = self.joke_manager.get_joke()
                    print(f"\n🎭 {joke['text']}\n")
                    
                    if self.config.audio_enabled:
                        audio_file = self.joke_manager.audio_manager.text_to_speech(joke['text'])
                        if audio_file:
                            self.joke_manager.audio_manager.play_audio(audio_file)
                
                elif command == 's':
                    self.joke_manager.save_jokes_history()
                    print("History saved!\n")
                
                elif command == 'h':
                    if self.joke_manager.jokes_history:
                        print("\n📜 Joke History:")
                        for joke in self.joke_manager.jokes_history[-5:]:
                            print(f"  {joke['id']}: {joke['text'][:50]}...")
                        print()
                    else:
                        print("No jokes in history yet.\n")
                
                elif command == 'c':
                    print(f"\n⚙️  Current Config:")
                    for key, value in asdict(self.config).items():
                        print(f"  {key}: {value}")
                    print()
                
                elif command == 'q':
                    break
                    
                else:
                    print("Invalid command. Try j, s, h, c, or q.\n")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error in interactive mode: {e}")
    
    def run_batch(self, count: int = None):
        """Run in batch mode"""
        if count is None:
            count = self.config.joke_count
            
        self.logger.info(f"Starting batch mode with {count} jokes")
        
        for i in range(count):
            if not self.running:
                break
                
            joke = self.joke_manager.get_joke()
            print(f"\n{i+1}/{count}: {joke['text']}")
            
            if self.config.audio_enabled:
                audio_file = self.joke_manager.audio_manager.text_to_speech(joke['text'])
                if audio_file:
                    self.joke_manager.audio_manager.play_audio(audio_file)
                    time.sleep(self.config.delay_seconds)
    
    def run_daemon(self):
        """Run as daemon/background service"""
        self.logger.info("Starting daemon mode")
        self.running = True
        
        # Start background audio playback
        self.joke_manager.audio_manager.start_background_playback()
        
        while self.running:
            joke = self.joke_manager.get_joke()
            self.logger.info(f"Generated joke: {joke['text']}")
            
            if self.config.audio_enabled:
                audio_file = self.joke_manager.audio_manager.text_to_speech(joke['text'])
                if audio_file:
                    self.joke_manager.audio_manager.audio_queue.put(audio_file)
            
            time.sleep(self.config.delay_seconds)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Advanced Joke Generator")
    parser.add_argument("--config", help="Configuration file path")
    parser.add_argument("--mode", choices=["interactive", "batch", "daemon"], 
                       default="interactive", help="Run mode")
    parser.add_argument("--count", type=int, help="Number of jokes for batch mode")
    parser.add_argument("--install", action="store_true", help="Install dependencies")
    parser.add_argument("--no-audio", action="store_true", help="Disable audio")
    
    args = parser.parse_args()
    
    # Initialize configuration
    config = Config()
    if args.config:
        config.config_file = args.config
    
    # Create app instance
    app = JokeGeneratorApp(config)
    
    # Load configuration
    app.load_config()
    
    # Override config with CLI args
    if args.no_audio:
        config.audio_enabled = False
    
    # Install dependencies if requested
    if args.install:
        app.joke_manager.install_dependencies()
        return
    
    # Load jokes history
    app.joke_manager.load_jokes_history()
    
    # Run based on mode
    try:
        if args.mode == "interactive":
            app.run_interactive()
        elif args.mode == "batch":
            app.run_batch(args.count)
        elif args.mode == "daemon":
            app.run_daemon()
            
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    finally:
        app.cleanup()

if __name__ == "__main__":
    main()
