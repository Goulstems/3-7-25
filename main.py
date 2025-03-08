# GOAL: Utilize file.readline() to read a WHOLE file line-by line! 

# GOAL: (soon) SORT contents of fakefile alphabetically

# ---

# consider other variations of operations we can do on files!

fileContents = open("fakefile.txt","r")
# print(fileContents.read())
print(fileContents.readline())
print(fileContents.readline())
fileContents.close()