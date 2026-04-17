#Reading from a file
file = open("myfile.txt", "r")
content = file.read()
print(content)
file.close()
# writing to a file
file=open("myfile.txt", 'w')
text=file.write("hello world!")
print(text)
file.close()
# writing to a file using append mode
file = open("myfile.txt", 'a')  
text=file.write("Hello, this is a test file.\n")
text=file.write("This is the second line.")
print(text)
file.close()  
