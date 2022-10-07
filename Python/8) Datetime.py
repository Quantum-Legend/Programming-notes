"""
For working with dates, you will need to import the datetime library into your program.
A library is a collection of precompiled routines and methods for you to use in your program.
Import is a function for making objects and libraries available to your program.
The import statement gives us access to the functionality of the datetime class
Without importing libraries, certain functions won't be available to you
"""
import datetime

currentDate = datetime.date.today()
#Dates can be stored in variables.
#today() is a function in date class that returns today's date
print(currentDate)
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)
#You can also access different parts of the date using .day, .month and .year
#Note: today() is a function, it takes in a value, does something to it, and returns the result as another value.
#That is why it uses parantheses.
#But day, month, year are properties, they only return a value.
#You can think of objects as nouns, then functions are verbs, they represent the object, or noun, doing something,
#or something being done with it. While the properties are adjectives, they describe how the object or noun is.
#For example, if there is a box, it has some properties which describe it, like it's length, breadth or height.
#A function would be doing something with the box, like opening it, putting something inside it, etc.

#Formatting dates!
#The default format of a date is YYYY-MM-DD
#We can use the strftime function to format how dates are displayed
print(currentDate.strftime("%d %b, %Y"))
#%d represents the day of the month, %b represents the abbreviation pf the month and %Y represents the 4-digit year.
#strftime stands for string from time
#Some more of the formats are:
#%d is the day of the month
#%b is the month abbreviation
#%B is the full month name
#%y is two digit year
#%Y is the 4-digit year.
#%a is the day of the week abbreviated
#%A is the day of the week
#For a full list visit strftime.org

print(currentDate.strftime("Today's date is %A, %B %d in the year %Y"))
#You can also display specific parts of the date as different parts of a whole string.
print()

#It is possible to force Python to use a particular language.
#To do this check out the babel Python library http://babel.pocoo.org/

#Now to input dates from the user, we must use the input().
#But, since the input function returns the value as a string data type, we also need to convert it into a date datatype.
#Let's ask the user for their birthday.
birthday = input("Please enter your birthday date (dd/mm/yyyy):")
#We should specify the format in our prompt so that the user inputs it in the right way.
#because if not, the code will crash and explode with errors.
#We should also be using some error handling, in the case that the user still doesn't enter the date in right format,
#But that will be covered in a later topic.

#Now to convert the input string to a date,
birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date() 
#The strptime function allows you to convert a string to a date 
#(I guess it stands for string put time? as in putting the string as a time?? Oh well, good for remembering though.)
#It takes in two arguments, the first is the string which you want to convert, and the other is the format
#of date in which you want to convert. (Here %m/%d/%Y will convert to a dd/mm/yy format) 
#Note:
#Why did we list datetime twice?  
#Because we are calling the strptime function 
#which is part of the datetime class 
#which is in the datetime module.
#The class is datetime, so the strptime coverts the string to a format of date and time combined
#To obtain only the date part of that, we use the .date() in the end

print(birthdate)

#Why do we need to go through the hassle to convert the string to a date?
#Because then we can use the various functions in the datetime module with the date datatype,
#which could be pretty useful.
#For example, you can show only the birth year and month from the input date.
print("The year in which you were born is " + birthdate.strftime("%Y") + " and the month was " + birthdate.strftime("%B"))
print()

#A more useful feature with date datatype, which makes it very worth to convert the string to a date
#is that you can subtract two dates to get back the number of days between those dates.
#For example, to calculate the number of days to your next birthday. I have covered that program
#in a different file (BirthdayCalculator.py)

#But just for an example,
DOB = datetime.datetime.strptime("03/04/2022","%d/%m/%Y")
#Initialising a birthday value
dateToday = datetime.datetime.strptime("12/12/2021","%d/%m/%Y")
#Initialising a current date value
difference = DOB - dateToday
print(DOB.strftime("If your birthday is on %d/%m/%Y") + dateToday.strftime(" and today's date is %d/%m/%Y"))
print("Then number of days until your birthday are", difference.days)
print()

#dates also allow you to use the timedelta function
#timedelta allows you to specify the time to add or subtract from a date 
print(currentDate + datetime.timedelta(days=15)) 
print(currentDate + datetime.timedelta(hours=15))
print()

#If datetime doesn’t have what you need, check out the dateutil library 
#(for example you might want to know the number of years between two dates instead of number of days)

#Since it is called Datetime, so yes, it can store times.
currentTime = datetime.datetime.now() 
print(currentTime) 
print(currentTime.hour) 
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime,"It is %I:%M:%S %p or %H%M hours and %S seconds"))
#%H is Hours (24 hr clock)
#%I is Hours (12 hr clock)
#%p is AM or PM
#%M	is Minutes
#%S is Seconds
