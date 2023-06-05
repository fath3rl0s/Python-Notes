#Exceptions and Error Handling
#Carlos Enamorado 


#Python does very little error checking at compile and execution times
#Python defers almost all checks on lines until line runs

#We can handle mistakes or exceptions, by using a try catch block
#Exception is just an error that results in a halt in execution




#Try Catch Block - Try block lets you test a block of code

#Accept Block - Lets you handle any errors

#Finally Block - executes regardless of the results of the try and accept blocks
#always executes





#Exceptions in Action
print("Exceptions")

print(1)
#IndentationError: unexpected indent
 #print(2)

#FileNotFoundError:
#f = open("A file that doesnt exist")


print("\n")


print("Try Block")
#Use a try block to remedy file not found error
#This is a catch all statement and does not target specific error
try:
	f = open("A file that does not exist")
except:
	print("File not available")


print("\n")


print("Improved Try Block to catch exceptions")
#We can tell python to error handle while also showing us the error
#This will not interrupt the code
try:

	f = open("A file that does not exit")
	anotherError

#Targeted error handling for 'f''
except FileNotFoundError:
	print("File does not exist")

#Generic error handle message for 'anotherError'
except Exception as e:
	print(e)

#Finally Message prints regardless of results
finally:
	print("Error Catch complete")

print("\n")


#Raise Exceptions
print("Raise Exceptions")

#only for this specific use case
#n = 0
#if n == 0:
	#raise Exception("n can not equal 0!")
#print(1/n)

#Output only catches int variable
#raise Exception("n can not equal 0!")




#Create exception that catches a string stored in 'n'
#Run this with int and string to confirm
n = 100
if n == 0:
	raise Exception("n can not equal 0!")
if type(n) is not int:
	raise Exception("n can not be a string! Must be int")
print(1/n)

print("\n")

#Assertions
#Similar to exceptions
#If Assertion expression fails
#an exception is raised and the program stops executing
#Assertion = Hard error checking
print("Assertions")

n = 1
assert(n != 0)
print(1/n)

#Output
#AssertionError



#Assertions and Exceptions are useful Python contructs
#for error handling and data verification

#When reading a file, instead of checking to see whether a file exists,
#we could just try to read it and then handle the exception
#in the case that it does exist

#Assertions can be used as shorthand if/else with hard error checking