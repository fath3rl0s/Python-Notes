#Reading and Writing Files
#Carlos Enamorado


#Python has standard functions for creating, reading and writing to files

#Iterate over a password file using python

#Read mode
print("Read Mode")

f = open("passExample.txt")
print(f)

#Output
# <_io.TextIOWrapper name='passExample.txt' mode='r' encoding='UTF-8'>

#Default mode of 'r' stands for read
#Will result in an error if it does not exist
#When working with files, we can specify different modes of operation 
#for our purposes


print("\n")


#Read Text mode
print("Read Text Mode")

f = open("passExample.txt", "rt")
print(f)


print("\n")


#Tell python concatenate file to terminal
print("F Read")

f = open("passExample.txt")
print(f.read())


print("\n")


#Do something specific with each line in the file
print("Read Lines")

#This creates an array and contains each line including carriage return 
f = open("passExample.txt", "rt")
print(f.readlines())


print("\n")


#Using readlines again will result in an empty array
#This happens because we have already read to the end of the file
print(f.readlines())


print("\n")


#To read again from the start, use 'seek' 
#Changes current file postion back to the zero byte (beginning)
print("Seek")

f.seek(0)
print(f.readlines())


print("\n")


#Iterate over each line in the file
#Using for loop
print("Iterate over Seek")

f.seek(0)
for line in f:
	print(line.strip())

#Useful if we want to read an existing file
#Could be used for a brute forcing POC


print("\n")


#Writing Files
#Open in write mode - 'w'
print("Writing Files")

f = open("writeTest.txt" , "w")
#write into the test we have opened for writing
f.write("This is a test line!")
f.close()

#Run again 
#'w' mode will overwrite the file, not append to it
f = open("writeTest.txt" , "w")
f.write("This is a test two!")
f.close()

#In order to Append, specify with 'a' mode
f = open("writeTest.txt" , "a")
f.write("\nThis is an append test!")
f.close()

#Confirm changes
f = open("writeTest.txt", "rt")
print(f.read())
f.close()


print("\n")


#If presented with a file handle and want more info on it
#call .name, .closed, .mode
print("File Information")

#File name
print(f.name)
#Whether or not the file was closed; True/False
print(f.closed)
#Mode last used in the script
print(f.mode)


print("\n")


#For larger files
#You can use the file object as an iterator for efficiency
print("Rockyou Password File")

#with open('/usr/share/wordlists/rockyou.txt') as f:
	#for line in f:
		#pass

#This will hit an error due to the encoding of some of the passwords
#UnicodeDecodeError: 'utf-8' codec can't...


#You will need to specify the encoding
with open('/usr/share/wordlists/rockyou.txt', encoding='latin-1') as f:
	for line in f:
		pass



