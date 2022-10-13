#use try except to catch error and prevent applications from crashing

try:
    income = int(input("Enter your income: "))
    expenses = 50
    result = expenses / income
    print(result)
except ZeroDivisionError:
    print("Income can't be 0")
