# This Is My 20th Python20.py File
# Reading Files
import time
info = "Reading Files From Python20.txt"
time.sleep(0.2)
print('\n\n',info.title(),"\n\n")



# reading file

python20txt_ =  open("Python-Master-Class/Python20.txt", "r") 

file = python20txt_.readlines()
print(file)
# To print line by line 
for textfile in python20txt_.readlines():
    print(textfile)




# write file 

txt_file = open("Python-Master-Class\Python20.txt", "w")
text_file = txt_file.write('''Hello My Name is Yogesh And I am 16 Year Old Boy.
\nI like Coding My Fav Machine Language is Python.
\nAnd i Know Little Bit HTML, AND CSS.I just Drop this Line from Python code\n''')

print(text_file)


# append file
txt_file = open("Python-Master-Class\Python20.txt", "a")
text_file = txt_file.write("\n\nI Just Drop This Line From Python Code.")
print(text_file)

txt_file.close()
python20txt_.close()

