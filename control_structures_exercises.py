
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

#Create an integer variable i with a value of 5

i = 5

#Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i in range(0, 101):
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -11:
    print(i)
    i = (i - 5)

#Create a while loop that starts at 2, and displays the number squared 
# on each line while the number is less than 1,000,000.

i = 2
while i < 1000000:
    print(i)
    i = i**2

#Write a loop that uses print to create the output shown below.
#100
#95
#90
#85
#80
#75
#70
#65
#60
#55
#50
#45
#40
#35
#30
#25
#20
#15
#10
#5

i = 100
while i > 0:
    print(i)
    i = i -5

# For Loops

#Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

#For example, if the user enters 7, your program should output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

i = input("What's your favorite number? ")
num = 1
for  num in range (1,10):
    product = (int(i)*num)
    print(i,"x",num,"=",product,)
    num = num + 1

#Create a for loop that uses print to create the output shown below.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

n = int(input("How many rows? "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#An Easier way

for r in range(1,10):
    print(str(r) * r)


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.


# STILL NEEDS WORK
n = int(input("Please enter an odd number between 1 and 50"))
for i in range (1,51,2):
    if n % 2 == 0:
        print(input("Invalid input"))
    print("Here is an odd number: ", i)

###Answer
print("Enter a whole odd number between 1 and 50")
pick = input()

if pick.isnumeric() == False:
    print()
    print("Please enter a WHOLE NUMBER!")
    print()

    continue

else:
    pick = int(pick)

if (pick < 51) and (pick %2 != 0):
    print()
    print(f"Thank you! Your number is: {pick}")
    print()

    break

else:

    print()
    print("Please Enter a number less than 50 and odd!")
    print()

for number in range(1,50):
    if number % 2 == 0:
        continue
    print("Here is an odd number:", number)


pick = 5

for number in range(1,50):
    if number % 2 == 0:
        continue
    if number == pick:
        print("Yikes! Skipping number:", number)
        continue
    print("Here is an odd number:", number)

#The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also 
# note that the input function returns a string, so you'll need to convert this to a numeric type.)

# STILL NEEDS WORK
n = int(input("Please enter an even number "))
for i in range (1,n+1):
    if n % 2 == 0:
        print(i)
        i = i + 1
    else:
        int(input("Please enter a valid number "))
        continue

###ANSWER

print("Enter a positive whole number!")
pick = input()

if pick.isnumeric() == False:
    print()
    print("Please enter a POSITIVE WHOLE NUMBER!")
    print()

else:

    pick = int(pick)

    print()
    print(f"Thank you! Your number is: {pick}"
    print()

    break #This gets us out of the function

for r in range (0,pick +1):
    print(r)



#Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

n = int(input("Please enter a postive integer "))
for i in range (n ,1):
    print i
    i = i-1


#FIZZ BUZZ

for r in range(1,101):
    if r % 15 == 0:
        print("FizzBuzz")
    elif r % 3 == 0:
        print("Fizz")
    elif r % 5 == 0:
        print("Buzz")
    else:
        print(r)











