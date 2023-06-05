#Conditionals
#Carlos Enamorado 


#Decisions based on the outcome of True or False

if True:
	print("True")

#This conditional is never printed because it is never false
if False:
	print("False")

if not False:
	print("not false")


print("\n")


#Extend conditionals to use comparisons
#This will not print because 1 is not less than 1
# Conditionals print when true
if 1 < 1:
	print("1 < 1")

#Check another evaluation
elif 1 <= 1:
	print("1 <= 1")

#Catch all statement using else
else:
	print("else 1")


print("\n")


#Create multiple comparisons
if 1 < 1:
	print("1 < 1")
elif 1 <= 1:
	print("1 <= 1")
elif 2 <= 2:
	print("2 <= 2")
else:
	print("else reached")

#The conditional continues until the True/False logic is hit
if 1 < 1:
	print("1 < 1")
elif 1 < 1:
	print("1 <= 1")
elif 2 <= 2:
	print("2 <= 2")
else:
	print("else reached")


if 1 < 1:
	print("1 < 1")
elif 1 < 1:
	print("1 <= 1")
elif 2 < 2:
	print("2 <= 2")
else:
	print("else reached")

#Else statement not needed


print("\n")


#Combine conditions with 'and'
#both statements must be true in order to print
if 1 > 0 and 0 < 1:
	print("1 > 0 and 0 < 1")


print("\n")


#OR operator
if 1 < 0 or 0 < 1:
	print("1 < 0 or 0 < 1")


print("\n")


#Combine 'and' // 'or' operators
if ( 1 < 0 or 0 < 1) and 1 == 1:
	print("Combined Operators")

if ( 1 < 0 or 0 < 1) and 1 == 0:
	print("This will not print because and statement is False")
print("\n")

if ( 1 < 0 or 0 < 1) or 1 == 0:
	print("This will print because second statement\ndoesnt need to be true")


print("\n")


#Spaces need to be consistent to avoid syntax errors
#Python does allow for conditional statements to be on the same line

if 1 > 0: print("Conditional statement on single line")


print("\n")


#Take a step further and use an inline ternary
#Ternary operator used to return a value based on the results of a conditional expression
#Instead of writing out an if/else block


if 0 < 1: print("Ternary Example")

print("1 >= 1") if 1 >= 1 else print("1 < 1")

#Re-write in more verbose way yet equivalent to above
if 1 >= 1:
	print("1 >= 1")
else:
	print("1 < 1")


print("\n")


# Create more complicated Ternary
print("More complicated Ternary Ahead")
print("\n")
print("Block Format")
if 0 > 1:
	print("1")
elif 0 < 1:
	print("2")
else:
	print("3")



print("\n")


print("Ternary Format")
print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")

#Conditonals enables us to do different things depending on results
#You may find ternarys in POCs, just remember to break them down
#They may be more efficient than block format
#Remember: Conditionals are checked in a linear order