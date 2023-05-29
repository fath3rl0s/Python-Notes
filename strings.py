#Strings
#Carlos Enamorado 


string1 = "I am a string"
string2 = 'Another string'

print(string1)
print(string2)

print("\n")

string3 = """This is 
a long 
string!"""

print(string3)


#Escape character \
string4 = "I\"m string"
print(string4)


#without escape character

string5 = "I'm not an escaped string!"
print(string5)

#Escape using hex
string6 = "\\ \x41\x42\x43"
print(string6)


string7 = "aaaaaaaaaa"
print(string7)


#OR

string8 = "a" * 10
print(string8)


#Builtin function to measure length of a variable
print(len(string8))
print("\n")


#check to see whether substring exists in a string
print("string" in string4)
print("hello" in string4)
print(string4.startswith("Test"))
print(string4.startswith("I\"m"))
print("\n")

#Identify index of string (starts counting at 0)
print(string4.index("string"))
print("\n")

#Modify strings 
print(string4.upper())
print(string4.lower())
print("\n")

#Parsing, cleaning up data
messy_string = "  Messy Strings with spaces!    "
print(messy_string)
print(messy_string.strip())
print("\n")

#Replace data
print(messy_string.replace("!","PPP"))

#You can chain fucntions
print(messy_string.replace("!","PPP").strip())
print("\n")

#Split strings to create a list 
print(messy_string.split())
#You can also denote where to split
messy_string2 = "  This is another,messy,string"
print(messy_string2.split(","))
print("\n")

#Encoding 
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))
print("\n")

#adjust left or right
print(string4.rjust(25))
print(string4.rjust(25,'x'))
print(string4.ljust(25))
print(string4.ljust(25,'y'))
print("\n")

#python strings are unmutable
#Concatenate into larger string 
# Int 'len(string4)' must be converted to string using 'str' function
print("String 4 is " + str(len(string4)) + " characters long")
print("\n")



print(type(1 + 1))
print(type("1" + "1"))
print("\n")


#Format method to improve and avoid errors
print("Format method to avoid errors")
print("String 4 is {} characters long".format(len(string4)))
print("\n")
print("{} {} {}".format(len(string4), len(string5), type(string3)))
#Also specify order
print("{0}, {2}, {1}". format(len(string4), len(string5), type(string3)))
#Also specify the name of the placeholder
print("{length}".format(length=len(string4)))
print("\n")

#You can do this without using the format method
length = len(string4)
print(f"string4 is {length} characters long!")
#Print as a float
print(f"string4 is {length:.2f} characters long!")
print(f"string4 is {length:.3f} characters long!")
print(f"string4 is {length:.4f} characters long!")
print("\n")

#Specify hex, binary and octal
print(f"string4 is {length:x} characters long!")
print(f"string4 is {length:b} characters long!")
print(f"string4 is {length:o} characters long!")
print("\n")

#Specify using data specifiers
print(f"string4 is %d characters long!" % len(string4))
print(f"string4 is %f characters long!" % len(string4))
print(f"string4 is %x characters long!" % len(string4))
