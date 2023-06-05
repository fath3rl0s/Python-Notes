#Lambdas
#Carlos Enamorado

#A Lambda is just an anonymous function that doesnt have a name
#It can have any number of arguments just like a normal function
#However, it can only have one expression

#For example, You cant use multiple lines in your anonymous lambda functions

print("Lambdas")


print("\n")

print("Single Argument")
add_4 = lambda x : x + 4
#Call anonymous lambda and pass for to 'x
print(add_4(4))


print("\n")


#Another with 2 arguments
print("Lambdas w/ Two Args")

add = lambda x,y : x + y
print(add(10,4))


print("\n")


#Expand the Lambda
print("Re-write // Expand Lambda")

def addf(x,y):
	return x + y

print(addf(10,4))


print("\n")


#We can also use anonymous expressions defined as part of the lambda
print("Anonymous Expression in Lambda")

print((lambda x, y: x +y)(10,4))


print("\n")



#Lambdas can be useful for short function expressions
#In hacking scripts, it may be useful to know whether a number is even or odd
print("Short Function Expression")

is_even = lambda x: x % 2 == 0
print(is_even(5))
print(is_even(4))


#This will return a True or False


print("\n")


print("Blocks w/ Lambdas")
#Another common hacking script lambda, is 
#The ability to break a string into blocks

blocks = lambda x,y: [x[i:i + y] for i in range (0, len(x), y)]
#Breaking up inputs into lists of a defined size
print(blocks("string",2))
print(blocks("strings", 3))


print("\n ")



#You may also see Lambdas used instead of maps
print("Lambdas v. Maps")

to_ord = lambda x: [ord(i) for i in x]
#Ord function returns the integer representation of each character
#The lambda provides a why to do this as a one liner!
print(to_ord("ABCD"))


print("\n")


#In case you are not comfortable with lambdas
print("Re-write this Ord Function")

def ord2(x):
	ret = []
	for i in x:
		ret.append(ord(i))
	return ret

#Same outcomes
print(to_ord("ABCD"))

#Lambdas can become harder to understand, maintain and/or modify with complexity
