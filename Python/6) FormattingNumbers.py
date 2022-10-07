"""
For the second example, let's just make a simple calculator!
We can get to know some of the different arithmetic operators in that way.
"""

#This is more of a shorthand way to directly convert the input number into a int or float data type.
print("Hello! Here is a simple calculator which operates on two numbers!")
no1 = float(input("Enter the first number: "))
no2 = float(input("Enter the second number: "))
#Here, we have just combined 2 functions in one line rather than doing "No1 = float(No1)"
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

#To display the message with the results, we can use the "," seperator in the print statement,
#since all the results would be float types (so + cannot be used).
print("The Sum of the two numbers is", add)
print("The Difference of the two numbers is", subtract)
print("The Product of the two number is", multiply)
print("The Quotient from the division of the two numbers is", divide)
print("The Remainder from the division of the two numbers is", remainder)
print("The Floor Value of the division of the two numbers is", floor)
print("(The floor value is the value of quotient rounded down to the nearest whole number)")
print()

#There are some other ways to display numbers in print(), wherein they can also be formatted.
print("I have %d pencils" % 12)
#%d is a placeholder in the string that tells it that a number is supposed to come there.
#This number (or variable containing that number) is written after the string following the % sign.
print("I also have %6d erasers" % 10)
#The '%6d' formats the number to get displayed with 6 spaces, the extra spaces will be to the left of the numbers
#So the number will appear right justified in a 6 space
print("And also %06d pens" % 8)
#The '%06d' here does the same thing as above, but the 0 in it makes it so that
#it has leading zeroes instead of empty spaces.
#The 'd' represents a decimal or integer value, which does not have a decimal point (yeah...)

#To format a float value, use 'f' instead of 'd'
print("%f is the sum of the two numbers" % add)
#A float number is shown with 6 decimal places by default,
#but using this formatting method, you can format it to show a specific number of decimal places.
print("%.2f is the difference of the two numbers" % subtract)
#This will display the number with 2 decimal places

#The other way to do this is by using the .format() method
print("{0:f} is the floor value from the division of the two numbers".format(floor))
#The whole '{0:f}' acts as the placeholder here. The curly braces represent this.
#The first part of the placeholder, the 0, is the index number that shows which position number
#is to be used from the arguments passed in the .format function.
#This is useful when you want to use more than one placeholder in the string, like:
print("{0:.2f} is the product of the two number and {1:.2f} is quotient from the division of the two numbers" \
      .format(multiply, divide))
#Here the '0' in the first placeholder represents that it is holding the place for the first
#argument of the .format(), and the '1' in the second placeholder represents it holds the place for
#the second argument of the .format(), i.e. multiply and divide respectively
#The second part of this placeholder is the same as the above method of formatting,
#it is used to tell what type of formatting you want there
#A little note:
#Here the \ was used tell python that i want to continue this command on the next line
#This can be used if the command gets too long to fit in one line so you can move onto the next line
print("{0:.3f} is the remainder from the division of the two numbers".format(remainder))
print()

# Some other formats:
print("Left padding with zeros:")
#make the total string size AT LEAST 9 (including digits and points), fill with zeros to the left
print('{:0>9}'.format(3.499))
#make the total string size AT LEAST 3 (all included), fill with zeros to the left
print('{:0>3}'.format(3))
print()

print("Right padding with zeros:")
# make the full size equal to 11, filling with zeros to the right
print('{:<011}'.format(3.499))
print()

print("Use commas as thousands separator:")
print("{:,}".format(10000000000))
print()