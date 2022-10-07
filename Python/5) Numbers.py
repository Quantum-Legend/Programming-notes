"""
One of the most useful things you can do in programming is calculations, and dealing with numbers in general.
As with a string, you can also store numbers in a variable and access it later.
You can use these variables to carry out mathematical calculations among other things.
"""

#There's something else you need to know about first though...
print("Let's add two numbers!")
no1 = input("Enter first number :")
no2 = input("Enter second number :")
add = no1 + no2
print("The two numbers added are " + add)
#When you execute the above block of code... a little problem arises
#The thing to note here is, the input() returns a string value, so the no1 + no2 concats the two strings, 
#instead of adding the two numbers.
#You can check that by using the type() function
print("The data type of no1 is ", type(no1))
print("The data type of no2 is ", type(no2))
#Here "," seperator is used to display the returned value of the type function.
#Another unseen issue here is you can't use that + in the print function here because it considers the 'add' variable
#as a string and concatenates them together. You can use the "," seperator though,
#but a few other things can also be used. Let's get to this later though.
print()

#Now to use numbers from user input as 'numbers', there are two ways,
#but both ways use the same category of functions.
#These functions are int(value), long(value), float(value), str(value).
#They convert the data type of the value or variable in their arguments to the data type of the respective function.
#That is, int will convert the value to the integer data type (positive or negative numbers without the decimal point),
#long to long integer (a bigger integer),
#float to a float data type (a number containing a decimal point, positive or negative)
#str to string data type

#The first way to do the above part of the code is this
add = float(no1) + float(no2)
#Now,
print("The data type of no1 is ", type(no1))
print("The data type of no2 is ", type(no2))
print("The data type of add is", type(add))
#Here we are changing the two entered numbers to float type before adding them.
#Then the added result is stored in the add variable which is a float type, as it should be,
#because of the data type conversion
print()
print("The two numbers added are", add)
#And voila! We get the correct answer!
print()
#You can also just change the variable's data type before adding them,
#so that all the three variables are in one type.
#For example,
no1 = float(no1)
no2 = float(no2)
print("The data type of no1 is ", type(no1))
print("The data type of no2 is ", type(no2))
print()

#Arithmetic operators are:
add = no1+no2
#Addition operator (+), Adds the numbers together
subtract = no1-no2
#Subtraction operator (-), Subtracts one number from another
multiply = no1*no2
#Multiplication operator (*), Multiplies the numbers
divide = no1/no2
#Division operator (/), Divides one number by another
exponent = no1**no2
#Exponentiation operator (**), Gives the exponent of the first number to the power of second number
remainder = no1%no2
#Modulo operator(%), returns the remainder of the division of no1 by no2
floor = no1//no2
#Floor Division operator (//), It rounds the result of the division of no1 by no2 down to the nearest whole number

#We have seen the '=' assignment operator, it assigns a value to a variable
a=10
print("a is", a)
#Lets say you want to add 20 to the value of a and store it back into a
#In this case, we can do:
a = a + 20
#This will add 20 to the previous value of a, i.e., 10 and store it back in a.
print("a+20 is", a, "which is again stored in a")
#This type of operations can be shortened by using the shorthand assignment operators
a += 20 #This has the same effect as a = a + 20
print("a += 20 is", a, "has the same effect as a = a+20")
#The other short hand operators are:
a -= 20 #Same as a = a - 20
print("a -= 20 is", a)
a *= 20 #Same as a = a * 20
print("a *= 20 is", a)
a /= 20 #Same as a = a / 20
print("a /= 20 is", a)
a %= 20 #Same as a = a % 20
print("a %= 20 is", a)
a **= 20 #Same as a = a ** 20
print("a **= 20 is", a)
a //= 20 #Same as a = a // 20
print("a //= 20 is", a)

#That's all for this program!
#The second shorthand way to do this + formatting the numbers in string will be covered in the next program
#which is FormattingNumbers