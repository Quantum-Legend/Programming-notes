"""
If you're going to code programs to solve different problems,
it will need to make decisions.
The choice made will depend on different conditions.
To implement this in our programs we use an if statement.
"""

#If statements allow you to specif code that only executes IF a specific condition is true
#The syntax of an if statement is:
'''
if <condition> :
    <block of code>
'''
#The colon is a part of the syntax and signifies the start of code block which is inside the if statement.
#The code block must be indented ahead of the if statement to be recognised as inside the if statement.

#For example:
answer = input("Would you like tea? ")
if answer == 'yes':
    print("That will be Rs. 20")
print("Have a good day!")
#Here, the program will ask the user a question, and only executes the print statement
#if the answer entered by the user is 'yes'. This is ensured by the if statement.
#The print statement "Have a good day" is outside of the if statement block,
#hence, it is always executed regardless of the user input

#Basically, the part of code inside an if statement is only executed when the if statement
#sees that the condition it is checking is true.

#You can see in the example above that the condition is represented by an expression
#answer == 'yes'
#Here, an equality check is being carried out by the relational operator (==).
#A relational or conditional operator is used in a conditional statement or expression
#such that the expression either returns a True value or a False value, depending on whether 
#the condition stated is satisfied or not
#Here, The expression will return True if answer is equal to the string 'yes',
#otherwise the expression will return False if that is not the case.
#The different relational operators are:
# ==    is equal to                      Returns true if operands are equal, else returns false
# !=    is not equal to                  Returns true if operands are not equal, else returns false
# >     is greater than                  Returns true if first term is greater than second, else returns false
# <     is less than                     Returns true if first term is less than second, else returns false
# >=    is greater than or equal to      Returns true if first term is greater than or equal to second, else returns false
# <=    is greater than or equal to      Returns true if first term is less than or equal to second, else returns false

