
# Conditional Basics

# Prompt for whether or not today is Monday
user_input = input("What day is today? ")
if user_input.lower() == "monday":
    print("Today is Monday! It's 1/7th of your life so make the best of it!")
if user_input.lower() in ["tuesday","wednesday","thursday","friday","saturday","sunday"]:
    print("Today is not Monday, have a great day!")
else:
    print("That's not a day!")

# Prompt for whether it's a weekday or weekend

user_input = input("What day is today? ")
if user_input.lower() in ["monday","tuesday","wednesday","thursday","friday"]:
    print("Today is a weekday!")
if user_input.lower() in ["saturday","sunday"]:
    print("It's the weekend, cheers!")
else:
    print("That's not a day!")

# Create variables and make up values
number_of_hours_worked_in_a_week = 42
hourly_rate = 50
this_weeks_paycheck = number_of_hours_worked_in_a_week * hourly_rate

def weekly_paycheck(n):
    hourly_rate = 50
    if n <= 40:
        print(n * hourly_rate)
    if n > 40:
        overtime_hours = n - 40
        overtime_rate = hourly_rate * 1.5
        overtime_pay = overtime_hours * overtime_rate
        print(overtime_pay + 2000)

weekly_paycheck(40)

# Loop Basics

# While

i = 5
while i <= 15:
    print(i)
    i += 1


i =0
while i in range(0, 101):
    print(i)
    i += 2
