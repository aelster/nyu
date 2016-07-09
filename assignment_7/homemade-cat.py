#!/usr/local/bin/python3

#def printFile(filePath): f = file(filePath) contents = f.read() printContents()
#def printContents(): print("Contents of " + filePath) print(contents)

def printFile(filePath):
    f = open(filePath,'r')
    contents = f.read()
    print("Contents of " + filePath);
    print(contents)

#================================================================================
printFile( "/home/vagrant/intro-programming/assignment_7/homemade-cat.py" )
