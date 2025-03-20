
def calculate_expenses(expenses):
    '''
    Args : expenses(list):
    A list of expese amount
    Returns:
        float : The total income sum of expenses
    '''
    return sum(expenses)

def calculate_income(incomes):
    ''' 
    Args : incomes(list):
    A list of incomes amount
    Returns:
        float : The total income sum of incomes
    '''
    return sum(incomes)
def calculate_savings(income, expenses):
    '''
    calculates savings based on income and expenses
    Args:
        income(float): The total income
        expenses(float): A list of expenses
    Returns:
        float: The total savings i.e income - expenses
    '''
        
    return income - expenses
        

