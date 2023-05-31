#Lists
#Carlos Enamorado 


#Another type of sequencee 
#ordered, changeable and allow for duplicates
#Use []

list1 = ["A", "B","C","D","E","F"]
print(list1)


print("\n")


#Can also have varying data types
#string, int, float, nested list, empty list, empty list (diff notation), tuple, boolean
list2 = ["A", 1, 2.0, ["B","C"], [], list(), ("A"), False]
print(list2)
print(type(list2))


print("\n")


#Can be indexed 
print(list1[0])
print(list1[1])
print(list2[4])
#last item
print(list1[-1])


print("\n")


#index nested list
print(list2[3][0])
print(list2[3][1])
#starting from the end
print(list2[3][-1])
print(list2[3][-2])


print("\n")


#Lists can also be changed by referencing the index 
#Changes "A" to "X"
list1[0] = 'X'
print(list1)


print("\n")


#To delete an index
del list1[0]
print(list1)


print("\n")


#To insert
list1.insert(0, "A")
print(list1)


print("\n")


del list1[0]
print(list1)

#Combine lists
list1 = ["A"] + list1
print(list1)

#Append
list1.append("G")
print(list1)


print("\n")


#Builtin in functions with lists
#Max and/or min
print(max(list1))
print(min(list1))


print("\n")


#find the index number of different items in the list
print(list1.index("C"))
#verify
#This is only saying print index '2' of list1 (C)
print(list1[list1.index("C")])
#same results here
print(list1[2])


print("\n")


#Reverse the list
list1.reverse()
print(list1)
#Reverse the reverse using slicee syntax
#[::-1] - start : stop : step
list1 = list1[::-1]
print(list1)


print("\n")


#Count Builtin
print(list1.count("A"))
list1.append("A")
print(list1.count("A"))


print("\n")


#Pop
#Remove the end of the list
print(list1)
list1.pop()
print(list1)


print("\n")


#Extend lists
list3 = ["H", "I", "J"]
print(list3)

list1.extend(list3)
print(list1)


print("\n")


#Finish and clear list; remove all values
list1.clear()
print(list1)


print("\n")


#Sort
list4 = [2, 5, 50, 16, 1]
print(list4)

list4.sort()
print(list4)

#reverse using slice
list4 = list4[::-1]
print(list4)
#reverse using method
list4.reverse()
print(list4)

#Or we can specify how to sort
list4.sort(reverse=True)
print(list4)


print("\n")


#You can not copy a list by saying list1 = list2
#You will need to make a copy because they will both reference the same underlying data
list5 = list4
print(list4)
print(list5)

#But what if we want to change a value in list5 and not list4
#This will change both list4 and list5 (referencing same data)
list5[2] = "X"
print(list5)


print("\n")


#work on same data but do different things
# make a copy

list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "Z"
print(list4)
print(list6)


print("\n")


#Use of the map function
#used to apply some function to all items to a list
list7 = ["1", "2", "3"]
print(list7)

#use map function to apply the float cast to each item
list8 = list(map(float, list7))
print(list8)#Use of the map function
