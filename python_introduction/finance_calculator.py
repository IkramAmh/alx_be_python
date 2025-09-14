month_income = int(input("Enter your monthly income: "))
month_expense = int(input("Enter your total monthly expenses: "))
month_saving = month_income - month_expense
projected_saving = int((month_saving * 12) + (month_saving * 12 * 0.05))
print("Your monthly savings are ", month_saving, "$")
print("Projected savings after one year, with interest, is: ", projected_saving, "$")