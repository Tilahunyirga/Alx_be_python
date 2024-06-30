monthly_income = int(input("enter your monthly income:"))
monthly_expense = int(input("enter your total monthly expense:"))

monthly_saving = monthly_income-monthly_expense;
print(f'your monthly saving are ${monthly_saving}')


project_savings = monthly_saving*12 + (monthly_saving*12*0.05);

print(f'project savings after one year ${project_savings}')