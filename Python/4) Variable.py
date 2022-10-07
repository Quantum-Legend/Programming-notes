"""
To have a user interaction with your program, one way is to use the input function.
The input function allows you to specify a message to display and returns the value typed in by the user.

The value that is entered by the user is stored in a variable (Here, name).
A variable is a kind of a placeholder for data values. It remembers the value entered by the user.
You can access this variable in different ways in your code.
For example, we can print the value in our variable name by using the print function.
"""

name = input("What is your name?")
print(name)

#A variable can be thought as a box, where you can store something and then come back to get it later.
#If you need to store more data, you can just create more variables.
#Like if you want to ask their name and roll no. for a school database.
#You can write a \n at the end of the prompt in input(), so that the input cursor comes on the next line of the message.
RollNo = input("What is your Roll No.?\n")
#Or you can just write a print statement with prompt before the input function to have the same effect
print(name)
print(RollNo)
#You can name your variable anything you like, as long as it isn't recognised by python as something else.
#Variable names can not contain spaces, they are case sensitive, and can not start with number.
#It's good to have variable names that are descriptive but not too long.

#To store values inside variables, the assignment operator '=' is used.
#The value stored in a variable can also be changed later in the code
name = input("Enter new name:\n")
RollNo = "69420"
print(name)
print(RollNo)
RollNo = input("Enter the new roll no. that you desire:\n")
print(name)
print(RollNo)
print()

#Variables can be combined with strings using the + sign (concatenation), as long as they contain a string value
print("Hello," + name + "your new roll no. is" + RollNo)
#You can add spaces as required
print("Hello, " + name +" "+ "your new roll no. is " + RollNo)
#Different parts of a string can also be combined by using the "," seperator in print()
print("Hello,", name, "your new roll no. is", RollNo)
#The "," seperator automatically puts the spaces between the string sub parts
#This is useful in print statements to use with variables that are not string type,
#as the + only concatenates two strings together.
print()

#Variables also allow you to manipulate the contents of the variable
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.swapcase())
print()
#lower(), upper(), swapcase(), capitalize(), etc are different python string functions.
#Because we are storing a string in the variable, we can use any of the Python string functions to manipulate the string.

#Some more of these functions are:
message = "hello world"

print(message.find("world"))
#It finds the position of the first letter of the sub string (part of a string) written in its parantheses,
#in the original string contained in the variable.
#Here, h is 0, e is 1, and so on, so the w of world comes at 6, therefore it returns 6.

print(message.count("o"))
#This function counts the number of times that character appears in the string in that variable.
#o appears in hello world 2 times, therefore it returns 2 here.

print(message.capitalize()) 
#This function makes the first letter of the string in upper case.
#The output here would then be Hello world.

print(message.replace("hello","hi"))
#As it says, this replaces one sub string with another in the string in that variable.
#The output here is hi world.
