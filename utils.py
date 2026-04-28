CATEGORY_NAME = ["Food", "Home", "Work", "Fun", "Misc"]
CURRENT_EXPENSES_FILEPATH = "current_expenses.csv"
ALL_EXPENSES_FILEPATH = "all_expenses.csv"
USER_FILEPATH = "user.csv"

def printChoices():
    print("1. Add expense")
    print("2. Change Savings")
    print("3. View Savings")
    print("4. Check Budget Status")
    print("5. Change budget")
    print("6. See top expenses")
    print("7. Exit")

def print_change_income_options():
    print("1. Add income")
    print("2. Deduct income")
    print("3. Set income")
    print("4. Exit")

def print_confirmation():
    print(green("1. Yes"))
    print(red("2. No"))
    print("3. Exit")
     
def print_categories():
    for index, category in enumerate(CATEGORY_NAME):
                        print(f"{index+1}. {category}")

    
def green(text:str) ->str:
    return f"\033[32m{text}\033[0m"

def red(text:str) ->str:
    return f"\033[31m{text}\033[0m"


def get_valid_float_input(custom_msg: str, custom_error_msg="hmm...that don't seem right. Please enter a number!!") -> float:
    float_input = input(custom_msg)
    while True:
        if not is_float(float_input):
            print(red(custom_error_msg))
            float_input = input(custom_msg)

        else:
            float_input = float(float_input)
            return float_input

def get_specific_valid_inputs(
        print_function, 
        custom_msg:str,
        valid_options: list,
        custom_error_msg="hmm...that don't seem right. Please enter a valid option!!"
    )->str:
        while(True):
                    print_function
                    specific_input = input(custom_msg)

                    if specific_input not in valid_options:
                        print(red(custom_error_msg))
                    else:
                        return specific_input

def is_float(value):
    try :
        float(value)
        return True
    
    except (ValueError,TypeError):
        return False
    