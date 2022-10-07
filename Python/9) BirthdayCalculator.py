"""
Let's calculate the number of days until your birthday!!
"""

import datetime

#Storing the current date value
currentDate = datetime.date.today() 

#User inputs their birthdate
birthday = input("Please enter your birthdate (dd/mm/yyyy):")
#Converting string to date datatype
birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

#Users birthday in the current year, created as a string from parts of the input 'birthdate' and initialized 'currentDate'
currentYearBirthday = birthdate.strftime("%d") + "/" + birthdate.strftime("%m")+ "/" + currentDate.strftime("%Y")
#Converting it back to date datatype
currentYearBirthdate = datetime.datetime.strptime(currentYearBirthday,"%d/%m/%Y").date()

nextYear = str(currentDate.year + 1) #Calculating the next year value as a string
#Users birthday in the next year
nextYearBirthday = birthdate.strftime("%d") + "/" + birthdate.strftime("%m") + "/" + nextYear 
#Back to date
nextYearBirthdate = datetime.datetime.strptime(nextYearBirthday,"%d/%m/%Y").date()

#Calculaation of difference of the birthdate in the current year with today
currentYearDifference = currentYearBirthdate - currentDate
#Calculaation of difference of the birthdate in the next year with today
nextYearDifference = nextYearBirthdate - currentDate

if int(currentYearDifference.days) == 0: #if no currentYearDifference, today is the birthday
    print("The number of days to your birthday is ", currentYearDifference.days)
    print("Happy Birthday to you!!")
elif int(currentYearDifference.days) > 0: #if positive currentYearDifference, birthday is still yet to come in the current year
    print("The number of days to your birthday is ", currentYearDifference.days)
    print("That is", currentYearDifference.days//7, "weeks and", currentYearDifference.days%7, "days")
else:
    print("The number of days to your birthday is ", nextYearDifference.days) #if negative currentYearDifference, birthday already happened in current year
    print("That is", nextYearDifference.days//7, "weeks and", nextYearDifference.days%7, "days")