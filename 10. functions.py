#Functions and Code Reuse
#Carlos Enamorado




#A function is a block of code that runs only when it is called
#This allows us to reuse code later on without having to re-write it




#We have already been using  builtin in functions such as 'print'
#But we can also define and use our own functions

#Useful, more effective, and less error prone than writing the same
#operations over and over again


#Functions
print("Functions")


print("\n")


#Define a Function
def function1():
	print("Hello, this is function1")

#Save and run as is
#This will not print until the function is called

#Call the function
#As is, we are not passing any arguments into the function
function1()

#Call the function again 
function1()


print("\n")


#Functions can also return a value
#This is useful if you want to use that result of that function for something else


#Return a Function's Value
print("Return:")


#Return
def function2():
	return "This is a returned value"

function2()

#Save and Run
#As is, this function2 will not print but store the value or returned the value


#Lets use the returned value
#Create a new variable set to function2
return_from_function2 = function2()
print(return_from_function2)


print("\n")


#You can also pass values to functions
print("Pass Values:")

#Create a new function that expects a variable as an input
def function3(s):
	#'\t' = tab
	#Print using format method
	print("\t{}".format(s))

#Call function3 and pass a parameter
function3("parameter")

#When run, we execute function3,
#Pass a parameter into it and it is stored as 's'
#Which we can then use within the function


#Running without passing an argument
#function3()

#Output:
# TypeError: function3() missing 1 required positional argument: 's'


print("\n")


#Functions can also accept multiple arguments
print("Multiple Arguments:")


def function4(s1, s2):
	print("{} {}".format(s1, s2))

function4("s1", "s2")

#These areguments can be anything
function4(3, 5)
#By defualt, s1 is first arg and s2 would be second arg
function4("any", "thing")



#When calling functions, you can specify keyword args
#By changing order of args being passed to function4
#This can override the default order
function4(s1 = "thing", s2 = "any")

#Order of variable doesnt matter
function4(s2 = "any", s1 = "thing")


print("\n")


#Assigning a defualt argument and changing on a later call
def function5(s1 = "default"):
	print("{}".format(s1))

function5()
function5("A different argument")


print("\n")


#We can also create functions that can handle an unknown or
#a variable amount of arguments

def function6(s1, *more):
	print("{} {}",format(s1, " ".join([s for s in more])))

function6


