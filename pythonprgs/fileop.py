# Open a file
fo = open ("foo.txt","a+")
print("Name of the file: ", fo.name)
print("Closed or not:", fo.closed)
print("Opening mode: ", fo.mode)
# Close opend file
str = input("Enter your input: ")
print("Received input", str)
fo.write(str)
fo.close ()