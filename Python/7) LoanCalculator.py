#A calculator to calculate loan!
print("Calculating your Monthly Payments")
L = float(input("Enter the amount of loan taken:\n"))
i = float(input("Enter the rate of interest at which the loan is taken (If rate is 5%, enter value as 0.05):\n")) 
n = float(input("Enter the number of monthly payments:\n"))

M = L*(i*(1+i)*n)/((1+i)*n-1)

print("The Monthly Payment amount is {0:.2f}".format(M))