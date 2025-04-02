from finance import calculate_expenses, calculate_income, calculate_savings

if __name__ == "__main__": 
    expenses = [1500, 200, 300]
    incomes = [4000, 1500]
    total_expenses = calculate_expenses(expenses)

    total_income = calculate_income(incomes)

    total_savings = calculate_savings(total_income, total_expenses)

    print(f"Total Expenses:  {total_expenses}")
    print(f"Total income : {total_income}")
    print(f"Total Savings: {total_savings}")