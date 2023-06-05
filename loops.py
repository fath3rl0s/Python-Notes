#Loops
#Carlos Enamorado 


#Increment a number by hand is impractical!
a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)


print("\n")


#While loop
print("While Loop")

a = 0
while a < 5:
	#Always include an exit condition! otherwise
	#not having 'a += 1' will create a never ending loop
	a += 1
	print(a)


print("\n")


#For Loop
#Executes a set number of times
print("For Loop")

#Iterate over each element in the list [0, 1, 2, 3, 4]
#Each of those values has been assigned a temporary value of 'i' in the loop
#So 0 + 6, 1 + 6, 2 + 6, etc...
for i in [0, 1, 2, 3, 4]:
	print(i + 6)


print("\n")


#As opposed to writing that out in long form
#We can make use of range
print("Range equivalent of above")
for i in range(5):
	print(i + 6)


print("\n")


#Nested Loops
print("Nested Loops")

for i in range(3):
	for j in range(3):
		print(i,j)

#The right hand column has the values for i
#The left hand column has the values for j

#Within the nested loop, i stays 0 until j meets its condition at 3

#First Iteration: i is zero, j is zero
#Second Iteration: i is zero, j is 1
#Third Iteration: i remains zero, j is 2; condition met at '3'

#4th: i increments by 1, j resets to 0
#5th: i is 1, j is 1
#And so forth until i meets it condition of 3 and the program exits


print("\n")


#Loop Control Statements
print("Break Control Statement")

for i in range(5):
	if i == 2:
		break
	print(i)


print("\n")


#We may not want to terminate loop early, use continue
print("Continue Control Statement")

for i in range(5):
	#This will skip 2
	if i == 2:
		continue
	print(i)


print("\n")


#Pass Control Statement
print("Pass Control Statement")

for i in range(5):
	if i == 2:
		pass
	print(i)


print("\n")



#You can loop over any iterable object you obtain an iterator from
#Loop over each character in a string
print("Loop over each character in a string")

for c in "example string":
	print(c)


print("\n")


#You can also do the same for a dictionary
print("Loop over dictionary")

for key, value in {"a":1, "b":2, "c":3}.items():
	print(key, value)

#Instead of needing to extract each value based on its key
#We can iterate over each item in sequence


print("\n")


#Another example using a predefined Dictionary
dict1 = {"x": 4, "y":5, "z":6}

for key, value in  dict1.items():
	print(key, value)