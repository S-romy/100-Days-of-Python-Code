print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill?: $"))
Tip = int(input("How much would you like to give? 10, 12, or 15?: "))
Number_of_people = int(input("How many people to split the bill?: "))

Tip_in_percent = Tip / 100
Total_tip_amount = Bill * Tip_in_percent
Total_bill = Bill + Total_tip_amount
Bill_per_person = Total_bill / Number_of_people

Rounded_figure = round(Bill_per_person, 2)

print(f"Each person should pay: ${Rounded_figure}")
