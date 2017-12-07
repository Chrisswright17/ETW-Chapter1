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

