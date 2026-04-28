from csv_file_writing import clear_csv, readfile, write_to_file
from expense import Expense
from user import User
from utils import ALL_EXPENSES_FILEPATH, CATEGORY_NAME,USER_FILEPATH, get_specific_valid_inputs, get_valid_float_input,green, print_categories, print_change_income_options, print_confirmation, printChoices, red

def main():
    user_info =readfile(USER_FILEPATH)

    if len(user_info) == 0:
            print("Welcome to your expense tracking app, where your spending finally makes sense.\n")
            surname = input("What is your surname: ").strip().capitalize()
            FirstName = input("What is your name: ").strip().capitalize()

            budget = get_valid_float_input(f"\nHello {FirstName}, what is your target budget: $")
            savings = get_valid_float_input("How much in savings do you have now: $")
            
            Main_user = User(FirstName,surname, budget, savings)
            write_to_file(USER_FILEPATH,[FirstName, surname, str(budget), str(savings)])


    else:
        user_info = user_info[0]
        Main_user = User(user_info[0], user_info[1], float(user_info[2]), float(user_info[3]))
        print(f"Welcome back {Main_user.FirstName}")

    while True:
        printChoices()
        print("\nSelect one of the options: ", end="")

        choice = input()
        while(choice not in ['1', '2', '3', '4', '5', '6', '7']):
            print(red("Hmm... that don't seem quite right. Please choose between 1 and 5.\n"))
            printChoices()
            choice = input("\nSelect one of the options: ")

        match(int(choice)):
            case 1:
                name = input("Name of expense: ").strip().capitalize()
                cost = (input("Cost: $").strip())

                while not is_float(cost):
                    print(red("Invalid value. Please enter a valid number!"))
                    cost = input("Cost: $").strip()

                print("Select a category")
                selected_index = get_specific_valid_inputs(print_categories(), f"Enter a category [1-{len(CATEGORY_NAME)}]: ", ['1','2','3','4', '5'],"Invalid category, try again!" )

                expense = create_expense(name, cost, int(selected_index))                
                Main_user.add_expense(expense, Main_user)

                print(green(f"{expense.name} expense added!\n"))


            case 2:
                while True:
                    print("\nWould you like to: ")
                    selected_index = get_specific_valid_inputs(print_change_income_options(), "Enter your choice: ", ['1', '2', '3','4'])

                    match(int(selected_index)):
                        case 1:
                            savings = get_valid_float_input("Enter the amout you would like to add to your current savings: $")
                            clear_csv(USER_FILEPATH, ['Name','Surname','Budget','Savings'])
                            Main_user.update_savings(savings, '+',Main_user)
                            print(green(f"Your savings is now: ${Main_user.savings:.2f}\n"))
                            break

                        case 2:
                            savings = get_valid_float_input("Enter the amout you would like to deduct from your current savings: $")
                            clear_csv(USER_FILEPATH, ['Name','Surname','Budget','Savings'])
                            Main_user.update_savings(savings,'-', Main_user)                            
                            print(green(f"Your savings is now: ${Main_user.savings:.2f}\n"))
                            break

                        case 3:
                            print(f"Your current total savings is : ${Main_user.savings:.2f}")
                            selected_index = int(get_specific_valid_inputs(print_confirmation(),"Are you sure you would like to proceed: ", ['1', '2', '3'] ))
                            
                            
                            match(selected_index):
                                case 1:
                                    savings = get_valid_float_input("Enter new savings amount: $")
                                    Main_user.set_saving(savings, Main_user)
                                    print(green(f"Your new savings amount is set to: ${Main_user.savings:.2f}\n"))
                                    break

                                case 2:
                                    print('\n')
                                    break
                                case 3:
                                    print('\n')
                                    break

                        case 4:
                            break         
            case 3:
                balance:float = Main_user.getBalance()

                if balance<50:
                    print(red(f"Your balance is ${balance:.2f}\n"))

                else:
                    print(f"Your balance is ${balance:.2f}\n")


            case 4:
                spendings = Main_user.get_total_spendings(ALL_EXPENSES_FILEPATH)
                status, amount = calculate_budget_status(Main_user.budget, spendings)

                if status == "within":
                    print(green(f"You are still left with ${amount:.2f}\n"))
                else:
                    print(red(f"You are overbudget by ${amount:.2f}\n"))
                    
            case 5:
                print(f"Your current budget is ${Main_user.budget:.2f}")
                selected_index = int(get_specific_valid_inputs(print_confirmation(), "Do you want to proceed to change your budget: \n", ['1', '2', '3']))
                while True:
                     match(selected_index):
                        case 1:
                            print(f"Your current budget is ${Main_user.budget:.2f}")
                            new_budget = float(get_valid_float_input("Enter new budget: $"))               
                            Main_user.change_budget(new_budget)
                            print(green(f"New budget changed to: ${Main_user.budget:.2f}\n"))
                            break
                        
                        case 2:break
                        case 3: break

                
               
            
            case 6:
                expenses = Main_user.get_expenses(ALL_EXPENSES_FILEPATH)
                if len(expenses) ==0:
                     print(red("No expenses added yet!!"))
                else:
                    print("\nYour top expenses are:\n")
                    expenses.sort(key=lambda x: x.cost, reverse=True)

                    #top 3 most expensive expense
                    if len(expenses) >3:
                        expenses = expenses[:3]


                    for index, expense in enumerate(expenses):
                        if index ==0:
                            print(red(f"{index+1}. {expense.name} (${expense.cost:.2f} for {expense.type})"))

                        else:
                            print(f"{index+1}. {expense.name} (${expense.cost:.2f} for {expense.type})")

                    print("\n")




            case 7: 
                print("Byeeeeeeee, see u soon!!")
                break

def is_float(value):
    try :
        float(value)
        return True
    
    except (ValueError,TypeError):
        return False
    
def create_expense(name: str, cost: str, category_index: int):
    if not is_float(cost):
        raise ValueError("Invalid cost")

    return Expense(
        name.strip().capitalize(),
        float(cost),
        CATEGORY_NAME[category_index - 1]
    )
    
def calculate_budget_status(budget: float, spendings: float):
    remaining = budget - spendings
    if remaining >= 0:
        return "within", remaining
    else:
        return "over", abs(remaining)




















if __name__ == "__main__":
    main()