revenue = int(input("Enter revenue "))
costs = int(input('Enter costs '))

difference = (revenue - costs)

if difference > 0:
    print("Sales plan completed")
    profit = difference/revenue
    print(profit)
    employees = int(input("Enter employees number"))
    bonus = difference/employees

    print(bonus)
else:
    print("Guys, we need to fire someone")