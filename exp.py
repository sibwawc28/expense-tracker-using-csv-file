import csv
from datetime import date

print("Welcome to Expense Tracker")

while(1):
    print("Enter number as per need ")
    print("1) Add Expense")
    print("2) Weekly Review")
    print("3) Exit")
    choice=int(input())

    match choice:
        case 1:
            print("Enter amount spent")
            amt=int(input())
            print("Enter description for expense")
            description=input()

            exp=[date.today(), amt, description]

            with open(r"e:\python fr\expense tracker\data.csv", "a", newline="") as csvfile:
                csv_writer=csv.writer(csvfile)
                csv_writer.writerow(exp)
             #newline will avoid line gaps
             #writerow, not writerows
             #writerows is for list of lists

            print("Expense saved")


        case 2:
            total=0
            count=0

            with open(r"e:\python fr\expense tracker\data.csv", "r") as csvfile:
                csv_reader=csv.reader(csvfile)
                for row in csv_reader:
                    if len(row)<3:
                        continue

                    amt=float(row[1])
                    total+=amt
                    count+=1

                if count>0:
                    average=total/count
                    print(f"Total expense = {total}")
                    print(f"Average expense = {average}")
                else:
                    print("No expense added yet.")


        case 3:
            exit()