import requests
from bs4 import BeautifulSoup
import time
import re

class OXAAMFetcher:
    def __init__(self):
        self.url = "https://oxaam.com/prxlycode5.php"
        self.session = requests.Session()
        # Add headers to mimic a real browser
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def get_latest_code(self):
        """Fetch the latest (top) OTP code from OXAAM"""
        try:
            response = self.session.get(self.url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()
            
            # Debug: Let's see what we're getting
            print(f"🔍 Debug - Full text content:")
            print(text_content[:500] + "..." if len(text_content) > 500 else text_content)
            print("\n" + "="*50)
            
            # Look for patterns like: 99tkq-iplqg, m05g2-cch30, he077-wm709
            # More specific pattern for the actual codes
            code_patterns = [
                r'[a-z0-9]{2,6}[-][a-z0-9]{2,6}',  # Pattern like: 99tkq-iplqg, m05g2-cch30
                r'[a-z]{2}[0-9]{3}[-][a-z]{2,3}[0-9]{2,3}',  # Pattern like: he077-wm709
                r'[0-9]{2}[a-z]{3}[-][a-z]{4,5}',  # Pattern like: 99tkq-iplqg
            ]
            
            all_found_codes = []
            
            for pattern in code_patterns:
                codes = re.findall(pattern, text_content.lower())
                all_found_codes.extend(codes)
            
            # Remove duplicates and filter out unwanted matches
            unique_codes = list(dict.fromkeys(all_found_codes))  # Remove duplicates while preserving order
            
            # Filter out date-like patterns and common words
            filtered_codes = []
            exclude_patterns = [
                r'\d{2}[-](jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
                r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[-]\d{2}',
                r'\d{1,2}[-](jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
            ]
            
            for code in unique_codes:
                is_date = False
                for exclude_pattern in exclude_patterns:
                    if re.match(exclude_pattern, code.lower()):
                        is_date = True
                        break
                
                # Additional filtering
                if not is_date and len(code) >= 6 and '-' in code:
                    # Make sure it's not a common word combination
                    parts = code.split('-')
                    if len(parts) == 2 and len(parts[0]) >= 2 and len(parts[1]) >= 2:
                        filtered_codes.append(code)
            
            print(f"🔍 Found potential codes: {filtered_codes}")
            
            if filtered_codes:
                return filtered_codes[0]  # Return the first valid code
            
            # If no codes found with patterns, try a broader search
            # Look for any sequence that looks like a code (avoiding dates)
            broad_pattern = r'[a-zA-Z0-9]{4,12}(?![-](jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec))'
            broad_codes = re.findall(broad_pattern, text_content, re.IGNORECASE)
            
            # Filter out common website text
            exclude_words = ['oxaam', 'inbox', 'date', 'code', 'usually', 'appears', 'within', 'seconds', 
                           'please', 'wait', 'page', 'refreshes', 'automatically', 'new', 'http', 'https']
            
            final_codes = [code for code in broad_codes 
                          if code.lower() not in exclude_words and len(code) >= 6]
            
            print(f"🔍 Broad search codes: {final_codes[:5]}")  # Show first 5
            
            if final_codes:
                return final_codes[0]
                
            return None
            
        except requests.RequestException as e:
            print(f"Network error: {e}")
            return None
        except Exception as e:
            print(f"Error parsing page: {e}")
            return None
    
    def monitor_codes(self, interval=15):
        """Continuously monitor for new codes"""
        print("🔄 Starting OXAAM code monitor...")
        print(f"⏱️  Checking every {interval} seconds")
        print("📋 Latest codes will appear below:\n")
        
        last_code = None
        
        while True:
            try:
                code = self.get_latest_code()
                
                if code and code != last_code:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    print("\n" + "🔥"*30)
                    print(f"🆕 NEW CODE FOUND!")
                    print(f"⏰ Time: {timestamp}")
                    print(f"🔑 CODE: {code}")
                    print("🔥"*30)
                    print(f"✅ Copy this: {code}\n")
                    last_code = code
                elif code:
                    print(f"⏳ [{time.strftime('%H:%M:%S')}] Current code: {code}")
                else:
                    print(f"❌ [{time.strftime('%H:%M:%S')}] No code found - retrying...")
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("\n🛑 Monitoring stopped by user")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(interval)

def main():
    fetcher = OXAAMFetcher()
    
    print("=== OXAAM OTP Code Fetcher ===\n")
    print("Choose an option:")
    print("1. Get current code once")
    print("2. Monitor codes continuously")
    print("3. Just show me the code now!")
    
    choice = input("\nEnter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        print("\n🔍 Fetching current code...")
        code = fetcher.get_latest_code()
        if code:
            print("\n" + "="*50)
            print(f"     LATEST CODE: {code}")
            print("="*50)
        else:
            print("❌ Could not fetch code")
            
    elif choice == "2":
        try:
            interval = int(input("Enter check interval in seconds (default 15): ") or "15")
            fetcher.monitor_codes(interval)
        except ValueError:
            print("Invalid interval, using default 15 seconds")
            fetcher.monitor_codes(15)
            
    elif choice == "3":
        print("\n🔍 Getting code right now...")
        code = fetcher.get_latest_code()
        if code:
            print("\n" + "🟢"*20)
            print(f"🔑 CODE: {code}")
            print("🟢"*20)
            print(f"✅ Copy this code: {code}")
        else:
            print("❌ Could not fetch code - try again!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()