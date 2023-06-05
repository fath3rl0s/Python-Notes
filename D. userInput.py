#User Input 
#Carlos Enamorado


#Prompt the user for input by using the input function
print("User Input")
test = input("Provide any IP:")
print(test)


print("\n")


#Combine information from before to improve script

#Infinite while loop because condition is always True
while True:
	test = input("Enter an IP:")
	
	#Print using format method
	print(">>> {}".format(test))

    #Provide a method for breaking loop
	if test == "exit":
		break
	#Else continue accepting user input / interation
	else:
		print("exploiting...")
