"""
\ (Backslash) is a special charcter used to type escape sequences in your string.
An escape sequence is a sequence of characters that does not represent itself
when used inside a character or string literal, 
but is translated into another character or a sequence of characters
that may be difficult or impossible to represent directly.
"""

#For example, \n is used to force the text to go to the next line.
print("This is the first line\nAnd this is the second line")
print()

#\t puts a tab space between the text.
print("This\tis a tab space")
print()

#\' and \" can be used to print that type of quote in the string.
#This is useful if you are using the same type of quotes to represent that string.
print('It\'s a fine day, ain\'t it?')
#A string enclosed in single quotes, containing single quotes.
print("\"Did you put your name in the Goblet of Fire, Harry?\", Dumbledore asked calmly")
#A string enclosed in double quotes, containing double quotes.
#Of course, there are other ways to get around this, which don't need you to use \ 
#but sometimes it may be necessary to do this.
print()

#A solitary backslash is no problem to display.
print("Here's a \ solitary backslash")
#but in case that \ is also recognised as part of an escape sequence, \\ can be used
#For example, if you want to display \news
print("Visit \news\today")
#This will consider the \n and \t as an escape character and not how intended.
#In such cases,
print("Visit \\news\\today")

"""
These are some examples of the special escape sequences used in programming
when dealing with string literals.
"""