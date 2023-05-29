#Booleans
#Carlos Enamorado 


valid = True
not_valid = False

print(valid)
print(not_valid)
print("\n")

#Compare Values
print(valid == True)
print(not_valid == True)
print("\n")

#More comparison tests
print(valid != True)
print(not_valid != True)
print("\n")

#Or shorthand
print(not valid)
print(not not_valid)
print("\n")

#Compare int
print((10 < 9) == True)
print((10 == 10 ) == True)
print((10 != 10) == True)
print((10 >= 10) == True)
print("\n")

#But we do not need to include '== True' for python to read
print((10 < 9) == True)
print((10 == 10 ) == True)
print((10 != 10) == True)
print((10 >= 10) == True)
print("\n")

#combine conditional statements with and/or
print(10 > 5 and 10 == 10 and 10 < 5)
print(10 < 9 or 10 > 5)
print("\n")

#Can also be referenced as numbers; 0 = false; 1 = true
print(bool(0))
print(bool(1))
print(bool(0) == False)
print(bool(1) == True)

#Evaluate arithmetic expressions
print(10 + 10)
print(10 - 10)
print(10 / 10)
#no float, largest possible integer using '//'
print(10 // 10)

print(10 /3)
print(10 // 3)
#Powers
print(10 * 10)
print(10 ** 10)
print(10 % 10)
print("\n")

x = 10
print(x)
x = x + 1
print(x)
#Shorthand
x += 1
print(x)
print("\n")
#same with other operations
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)
print("\n")

#binary
x = 13
print(bin(x))
#make easier to read by removing '0b' and using right adj to make sure value is always 4 bits in length
print(bin(x)[2:].rjust(4,"0"))


y = 5
print(bin(y)[2:].rjust(4,"0"))
print("\n")

#You may see in exploits or POC
#Bitwise AND comparison; checkiing when both bits are set to '1'
# 13 bitwise anded with 5 = 5 in binary
print(bin(x & y)[2:].rjust(4,"0"))

#Bitwise OR; 1 or 1 = 1; 1 or 0 = 1 etc
print(bin( x | y)[2:].rjust(4,"0"))
print("\n")

#bit shifts
#x=13
#move all bits over by 1
print(bin(x)[2:].rjust(4,"0"))
print(bin(x >> 1)[2:].rjust(4,"0"))
print(bin(x >> 2)[2:].rjust(4,"0"))
print(bin(x >> 3)[2:].rjust(4,"0"))
print(bin(x >> 4)[2:].rjust(4,"0"))
#Opposite Direction
print(bin(x << 3)[2:].rjust(4,"0"))
print(bin(x << 2)[2:].rjust(4,"0"))
print(bin(x << 2)[2:].rjust(4,"0"))
