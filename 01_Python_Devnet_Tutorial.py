            #Devnet Fieldtrip Python Notes#
                #Date: 12/07/2017#
                    #Notes Taken By Chrias#


#Most basic command is print#
print('DEVNET Is Cool')
#defining variables#
str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print(space)
#Conversions#
#int to str conversion#
x=3
print("The value of x is " + str(x))
print(space)
#x=str(x)Converts the predefined variable "x" from an int type into a str type#

#Lists:#
#make a list using [] ex:
hostnames=["apple","pear","cat"]
print(hostnames)
print(space)
#del hostnames[1] deletes the item in the 1st spot of the list. lists go: 0, 1, 2, 3, 4, 5 etc#
#in a list all the items have to be the same type but in a tuple you can have the items be different types#
list=[12,4,19,96,12]
print(list)
print("The output for list[-1] is " + str(list[-1]))
print("The output for list[2] is " + str(list[2]))
print(space)

#Dictionaries#
ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
#This format is the text in the first set of quotes is the value or identifier.#
#The text in the second quotes is the value of the identifier.#
print(ipAddress)
print(type(ipAddress))
print(space)
print("typing ipAddress['R1'] will give the value for the specified keyword ex: ")
print(ipAddress['R1'])
print(space)
#To add a key/value pair by setting the new key equal to a value#
ipAddress["S1"]="10.1.1.10"
print(ipAddress)
print("R3 in ipAddress gives the output:")
print("R3" in ipAddress)
print(space)
#Input Function#
#The input() function provides a way to get information from the user#
firstName = input("what is your firstname? ")
print("Hello " + firstName +"!")
print(space)
#If/Else Functions#
nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
#If the nativeVLAN is equal to dataVLAN print that native and data VLAN are equal. ELSE (if its not equal)#
#print this native and data VLAN are different#
else:
    print("This native VLAN and the data VLAN are different.")
print(space)
VLAN1 = input("What is the value of VLAN1? ")
VLAN2 = input("what is the value of VLAN2? ")
if VLAN1 == VLAN2:
    print("VLAN1 and VLAN2 are equal!")
else:
    print("VLAN1 and VLAN2 are not equal!")
print(space)
#If/Elif/Else Function#
#What the Elif function does is first does a normal IF function then if that IF function is not met it goes onto a second if statement#
#If the second IF statement is met then it goes on like a normal IF function#
#If neither of the IF statements are met then it procceeds to go the the Else statement and proceed as a normal if/else function#
ExampleNumber = int(input("What is your number? "))
if ExampleNumber >= 1 and ExampleNumber <=99:
    print("This number is between 1 and 99")
elif ExampleNumber >=100 and ExampleNumber <=199:
    print("This number is between numbers 100 and 199")
else:
    print("This number is neither between numbers 1 and 99 or 100 and 199.")
print(space)
#Operations#
#Python is able to do several math operations#
#Addition
print("2 + 5 = " + str(2 + 5))
#Subtraction#
print("2 - 5 = " + str(2 - 5))
#Multiplication#
print("2 * 5 = " + str(2 * 5))
#Division#
print("6 / 3 = " + str(6 / 3))
#Modulo#
#Modulo returns the remainder from the division of two numbers#
print("3 % 2 = " + str(3 % 2))
