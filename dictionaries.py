#Dictionaries
#Carlos Enamorado 


#Store vaues in key : value pairs
#Uses curly braces

dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))


print("\n")


#Access item's value in a dictionary
print(dict1["a"])
print(dict1.get("a"))


print("\n")


#cannot be called by index; python cant find this key
#print(dict1[0])


#Print all of the keys
print(dict1.keys())

#Print all values in the dictionary
print(dict1.values())

#Print all of of the items; keys and values
print(dict1.items())


print("\n")


#Doesnt allow duplicates
#Cannot add another key of 'a' if 'a' already exists
dict1["a"] = 1
print(dict1)

#You can add new items
dict1["d"] = 4
print(dict1)


print("\n")


#you can change and items value
dict1["a"] = 0
print(dict1)
#You can use update method
dict1.update({"a":15})
print(dict1)


print("\n")


#Remove using pop
dict1.pop("d")
print(dict1)
#Del syntax
del dict1["a"]
print(dict1)


print("\n")


#nested dictionary
dict1['c'] = {"x":0, "y":1,"z":2}
print(dict1)


print("\n")


#Empty dictionaries
#Two ways to complete
#Useful when you know you want to use a dictionary data structure
# But you dont know what the data is just yet
# when you are iterating against some structure and you want to be able to have 
# a quick look up based on some key
dict2 = {}
dict3 = dict()
print(dict2)
print(dict3)


print("\n")

