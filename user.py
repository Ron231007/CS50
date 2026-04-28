from csv_file_writing import readfile,write_to_file,clear_csv
from expense import Expense
from utils import CURRENT_EXPENSES_FILEPATH,ALL_EXPENSES_FILEPATH,USER_FILEPATH

class User:

    income=0

    def __init__(self, FirstName: str,surname:str, budget:float, savings:float):
        self.FirstName = FirstName
        self.surname = surname
        self.budget = budget
        self.savings = savings

    def set_saving(self, savings:float, user_info):
        self.savings = savings
        clear_csv(CURRENT_EXPENSES_FILEPATH,['Name', 'Cost', 'Type'])
        clear_csv(USER_FILEPATH, ['Name','Surname','Budget','Savings'])
        write_to_file(USER_FILEPATH,[user_info.FirstName, user_info.surname, user_info.budget, self.savings])

    def update_savings(self, savings:float, operator:str,user_info):
        if operator == '+':
            self.savings+=savings

        else:
            self.savings-=savings

        write_to_file(USER_FILEPATH,[user_info.FirstName, user_info.surname, user_info.budget, self.savings])

    def get_total_spendings(self,filename:str):
        expenses = self.get_expenses(filename)
        return sum([x.cost for x in expenses])

    def getBalance(self):
        return self.savings
    
    def add_expense(self,expense: Expense, user_info):
        self.savings-=expense.cost
        clear_csv(USER_FILEPATH, ['Name','Surname','Budget','Savings'])
        write_to_file(USER_FILEPATH,[user_info.FirstName, user_info.surname, user_info.budget, self.savings])

        write_to_file(CURRENT_EXPENSES_FILEPATH, [expense.name, str(expense.cost), expense.type])
        write_to_file(ALL_EXPENSES_FILEPATH, [expense.name, str(expense.cost), expense.type])

    def is_within_budget(self) ->bool:
        spendings = self.get_total_spendings(CURRENT_EXPENSES_FILEPATH)
        return spendings<self.budget
        
    def change_budget(self, new_budget:float) ->None:
        self.budget = new_budget
        

    def get_expenses(self,filename:str) ->list:
        expenses = []
        expenses_data = readfile(filename)        
        for expense in expenses_data:
            #Skip empty line
            if len(expense) ==0:
                continue
            new_expense = Expense(expense[0], float(expense[1]), expense[2])
            expenses.append(new_expense)

        return expenses
