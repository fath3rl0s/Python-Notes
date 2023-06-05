#Comprehensions
#Carlos Enamorado


#Comprehensions provide a shorter syntax to create lists over some iterables

#Fist take a list
list1 = ["a", "b", "c"]
print(list1)


print("\n")


#Now that we have an iterable we can create a
#Comprehension
print("Comprehension")

#Iterating over each element in list1
#Adding into list2
list2 = [x for x in list1]
print(list2)


print("\n")


#Use Conditionals with Comprehensions
print("Comprehension w/ Conditionals")

#Iterates over each element in list1
#If x == 'a' anywhwere in list1, add to list3
#Print list3
list3 = [x for x in list1 if x == 'a']
print(list3)


print("\n")


#Work with other iterables such as Ranges
print("Comprehension w/ Range")

#Iterate over each int in range(5) and
#Assigns x to that value while adding to list4
list4 = [x for x in range(5)]
print(list4)


print("\n")


#Apply some function
print("Apply Function to Comprehension")

print("HEX")
list5 = [hex(x) for x in range(5)]
print(list5)

print("BINARY")
list5 = [bin(x) for x in range(5)]
print(list5)


print("\n")


#Comprehension with Ternary Conditionals
print("Comprehension with Ternary Conditionals")

#If x > 0, convert to hex equivalent
#else, change to 'X'
list6 = [hex(x) if x > 0 else 'X' for x in range(5)]
print(list6)


print("\n")


#Perform other Operations
print("Other Operations w/ Comprehension")


list7 = [x * x for x in range(5)]
print(list7)


print("\n")


#Expand on Simple Conditionals
print("Expand on Simple Conditionals")


list8 = [x for x in range(5) if x == 0 or x == 1]
print(list8)


print("\n")


#Can also work with nested expressions
print("Comprehension w/ Nested Expressions")

#Nested List (list within a list)
list9 = [[1,2,3], [4,5,6], [7,8,9]]
print(list9)

#This creates on singles list from a nested list
#Take the list from elements y,
#Form the nested list x,
#And create a new list of each y that are in x
list10 = [y for x in list9 for y in x]
print(list10)


print("\n")


#Comprehensions w/ Other Iterable data types like we saw with range
print("Comprehension w/ Sets")

set1 = {x + x for x in range(5)}
print(set1)


print("\n")


#Create a list made up of characters in a string
print("Comprehension and Strings")

list11 = [c for c in "strings"]
print(list11)


print("\n")


#You may see list comprehensions used with the join method
#Join is used to combine items in an iterable into a single string
print("Comprehension w/ Join Function")

#Take the previous list11 and join the characters
print("".join(list11))

#You can also add a delimeter between the items
print("-".join(list11))


print("\n")


#Comprehensions provide another way to write in shorthand in python
#Comprehensions can also be written out in longer formats


#Longer Format Example
print("Longer Format")

list12 = []
for c in 'strings':
	list12.append(c)
print("-".join(list12))
