#Tuples
#Carlos Enamorado 


#Immutable and can not be changed
#Use () and surround with double quotes

items = ("item1", "item2", "item3")
print(items)
print(type(items))


print("\n")

#can also be numbers
tuples_numb = (1, 2, 3)
print(tuples_numb)
print(type(tuples_numb))


print("\n")


#Repeat tuples
# if comma not iuncluded, it will repeat as string **
tuple_repeat = ("Repeat this Tuple!",) * 4
print(tuple_repeat)
print(type(tuple_repeat))


print("\n")


#mixed tuples
#combine string, int, and nested tuples
tuples_mixed = ("A", 1, ("B", 2))
print(tuples_mixed)
print(type(tuples_mixed))


print("\n")


#can be combined but not changed
#can not append to existing tuple

#tuples_mixed.append("item4") - this will error
# AttributeError: 'tuple' object has no attribute 'append'

#You can combine 
tuple_combined = tuples_numb + tuple_repeat
print(tuple_combined)
print(type(tuple_combined))


print("\n")


#Can be useful to unpack all in one line

item1, item2, item3 = items
print(item1)
print(item2)
print(item3)


print("\n")


#Whether items exist in an item or not
print("item2" in items)
print("item3" in items)
print("item5" in items)


print("\n")


#index of the match
print(items.index("item2"))

items = ("item1", "item2", "item3")
print(items[0])
print(items[1])
print(items[2])


print("\n")


#find out bhow long tuple is
print(len(items))


print("\n")


#Print last item only using -1 index
print(items[-1])
#or second to last using -2
print(items[-2])


print("\n")


#slices to extract a number of elements from the start of slice up to but not including the end
print(items[0:2])
#OR - same thing
print(items[:2])


print("\n")


#count form the end using slicing
print(items[-3:-1])


print("\n")


#index access

string1 = "I am a string!"
#everything until 4th character
print(string1[0:4])
#everything except last chacacter
print(string1[:-1])
#only the last character
print(string1[-1])