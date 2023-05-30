#Variables and Data Types
#Carlos Enamorado




name = "carlos"
print(name)

name_length = 6
print(name_length)

#same-line variable assignment
name, name_length = "carlos", 4


# Print variable and its data type
print(type(name))
print(type(name_length))


#List defined with []

name_list = ["carlos", "123CTF", "acbcd"]
print(type(name_list))

#unpack list
name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)



#Tuple defined with ()

name_tuple = ("tuple", "4321")
print(type(name_tuple))


# Dictionary defined with {}

name_dictionary = {"Dick": 1, "1234": 6}
print(type(name_dictionary))

print(name_dictionary)



# Boolean

name_boolean = True
print(type(name_boolean))
print(name_boolean)

# Range 
name_range = range(6)
print(type(name_range))
print(name_range)


# Bytes

name_bytes = b"carlos2"
print(type(name_bytes))



# Print all
print("\n")
print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_boolean)
print(name_range)
print(name_bytes)
