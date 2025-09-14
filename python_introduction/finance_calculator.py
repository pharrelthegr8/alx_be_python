income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)

print (f"Your monthly savings are ${monthly_savings}")
print (f"projected savings after one year, with interest, is: ${projected_savings}")
