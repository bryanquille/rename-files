import os

location = input("Type a directory:  ")
content = os.listdir(location)
newName = input("Type the new name for files:  ")
fileExtension = input("Give the file extension (eg. .txt, .jpg):  ")
sequence = 1
for i in content:
    completeNewName = newName + "_" + str(sequence) + fileExtension
    lastFile = os.path.join(location, i)  
    newFile = os.path.join(location, completeNewName)
    os.rename(lastFile, newFile)
    sequence += 1

print("Files were rename correctly.")