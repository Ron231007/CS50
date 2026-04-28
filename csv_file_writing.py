import csv

from expense import Expense

def write_to_file(filename:str, expense:list[str])->None:
    with open(filename, 'a', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(expense)
        

def readfile(filename:str) ->list[list]:
    content = []

    with open(filename,'r', newline="" ) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            content.append(row)

    return content[1:] if len(content)>1 else []

def clear_csv(filename:str, hedaer:list[str]) ->None:
    with open(filename,'w', newline="" ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(hedaer)
