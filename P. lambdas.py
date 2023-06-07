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

print((lambda x, y: x + y)(10, 4))


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


'''
Imagine you have a long string of numbers: "1234567890".

Now, let's say you want to divide this string into smaller blocks of size 3. The lambda function you provided, blocks = lambda x, y: [x[i:i + y] for i in range(0, len(x), y)], can help you achieve that.

Here's a step-by-step explanation of how it works:

The lambda function takes two inputs: x (the long string of numbers) and y (the desired block size, which is 3 in our example).

The range(0, len(x), y) part generates a sequence of numbers starting from 0 and incrementing by y each time. In our example, it generates the sequence: 0, 3, 6, 9. These numbers represent the starting indices of the blocks in the original string.

The lambda function then iterates over the generated indices using a list comprehension. For each index i, it slices the original string x to extract a block of length y. In our example, it slices the string as follows:

For i = 0, it takes the slice x[0:3] and gets the block "123".
For i = 3, it takes the slice x[3:6] and gets the block "456".
For i = 6, it takes the slice x[6:9] and gets the block "789".
For i = 9, it takes the slice x[9:12], but since the string ends before index 12, it just takes the remaining part "0".
The resulting blocks "123", "456", "789", and "0" are collected in a list, which is then returned by the lambda function.

So, when you apply this lambda function to the string "1234567890" with a block size of 3, it will return a list of blocks: ["123", "456", "789", "0"].
'''


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
