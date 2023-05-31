#Sets
#Carlos Enamorado 


#Store multiple values in one variable
#Cant be ordered and dont allow duplicate values
#Use curly braces
#Looks similar to a dictionary although does not utilize key value pairing

#Carlos Enamorado

set1 = {"a", "b", "c"}
print(set1)
print(type(set1))


print("\n")


#Running this again will  show a different order of 'a, b, c'
#This is because sets are not ordered! 
# Example: 'a, b, c' - 'b, a, c' - etc


#Because sets are not ordered, we cant use indexes with sets
#print(set1[0])
#this will errors out 
#TypeError: 'set' object is not subscriptable

#Sets can not have duplicates, this will show only one value
set2 = {'a', 'a', 'a'}
print(set2)
#Confirm by checking for set length
print(len(set2))


print("\n")


#Sets can be made up of any data types
set3 = {'a', 3, True, 5.2}
print(set3)


print("\n")


#We can use a set constructure to create sets
set4 = set(("b", 1, False))
print(set4)


print("\n")


# Add to a set using ADD
set1.add('d')
print(set1)

#You can also update existing set
set3.update("xyz")
print(set3)

set3.update(set4)
print(set3)

#Because sets cannot have duplicates, we will not print '1' because in boolean
#True = 1; set3 already 'True' so it will not add set4 '1'


print("\n")


#Possible to update sets with different kinds of iterables
list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)


print("\n")


#Create a set Union
set5 = {11, 12, 13}
set6 = set4.union(set5)
print(set6)


print("\n")


#Remove values in set
print(set6)
set6.remove('b')
print(set6)
#**Remove will shoot an error if the value does not exist**


print("\n")


#To avoid the error, use discard
print(set6)
set6.discard('b')
print(set6)


print("\n")


#You can also use pop
#But can give unexpected results because sets are not ordered!
#Only use when you dont care with values need to be removed

print(set1)
set1.pop()
print(set1)
#This will change each time the program is run