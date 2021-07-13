# 1
# Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or 
# the string 2, False otherwise.

# function accepts one input and return True if the passed input is either the number or 
# the string 2, False otherwise.
def is_two(n):
    # checks to see if the passed argument is 2 or the string 2 and returns True if so
    if n == 2 or n == "2":
        return True
    # return False if the parameters are not met
    else:
        return False

is_two(2)
is_two('2')
is_two('something else')

# 2
# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

# accepts a string as the paramter
def is_vowel(string):
    # check each character in the string and see if it's a vowel
    if any(ch in 'aeiou' for ch in string.lower()):
        return True
    else:
        return False

is_vowel("saxophone")
is_vowel("sxphn")

# 3
# Define a function named is_consonant.
# It should retun True if the passed string is a consonant, False otherwise.

def is_consonant(string):
    # checking to see if characters in string are in vowels
    # this time returning false if they are
    if any(ch in 'aeiou' for ch in string.lower()):
        return False
    else:
        return True

is_consonant("saxophone")
is_consonant("sxphn")

# 4
# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the 
# word if the word starts with a consonant.

def capitalized_consonant(string):
    # checks to see if the first letter of the string is a vowel
    if str[0] in "aeiouAEIOU":
        return str
    # if its not, return the string with the first letter capitalized
    else:
        return str.capitalize()


capitalized_consonant("saxophone")

# 5
# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

# takes in two arguments, the tip amount as a decimal and the bill
def calculate_tip(tip,bill):
    # calculates what the tip amount should be and adds it to the bill total
    return (tip * bill) + bill
# another option is entering the tip as a whole number and divide it by 100

# I did calculate the total bill...need to adjust
calculate_tip(.2,20)

# 6
# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

# takes in the total price and percentage as a decimal
def apply_discount(price,percentage):
    # returns the total price minus how much the discount is worth
    return price - (price*percentage)

apply_discount(100,.1)

# 7
# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.

# takes in a string
def handle_commas(string):
    # replaces any commas with '' to remove the commas
    output = str(string.replace(',',''))
    return output

handle_commas('1,000,000')

#another way
def handle_commas(string):
    number = ""
    for char in string:
        if char not in ",":
            number += char
    return float(number)

# 8
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    # defines the letter grade range, used 101 because range is high value exclusive
    if number in range(90,101):
        return 'A'
    # used elif statements to continue through the code if the first parameter is not met
    elif number in range(80,89):
        return 'B'
    elif number in range(70,79):
        return 'C'
    elif number in range(60,69):
        return 'D'
    # everything below a 60 is considered an F
    else:
        return 'F'

get_letter_grade(100)

# 9
# Define a function named remove_vowels 
# that accepts a string and returns a string with all the vowels removed.

# takes in a string
def remove_vowels(string):
    # creates a result variable that iterates through each 
    # character in the string that's not a vowel
    result = [ch for ch in string if ch.lower() not in 'aeiou']
    # replace the vowel with '' to remove any space
    result = ''.join(result)
    return result

remove_vowels('hello')

# 10
# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

#NOT FINISHED
def normalize_name(string):
    output = string.strip().replace(' ','_').lower()
    return output

# ANSWER?
def normalize_name(name):
    cleaned = ""
    for char in name:
        if (char.isalnum() == True) or (char == " "):
            cleaned += char
    return cleaned

normalize_name('    CAPITALIZED WITH SPACES    ')


# 11
# Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumulative_sum(list):
    # create a list to store the new list
    cumulative_list = []
    # create a variable to use to add to each element in the list
    total = 0
    # i is a variable that will iterate through each element in the list
    for i in range(0,len(list)):
        # the item in each list position is added to total
        total+=list[i]
        # add the item to the cumulative list
        cumulative_list.append(total)
    # return the cumulative list after the program has gone through each item
    return cumulative_list

cumulative_sum([5,10,20])

# Bonus 1 Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm 
# and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.


#STILL NEEDS SOME TWEAKING

# takes in a time string
def twelveto24(string):
    # checks to see if its am, and starts with 12 
    if string[-2:] == 'am' and string[:2] == '12':
        # replace the 12 with 00 since its 24 hour format
        return '00'+string[2:-2]
    # if its am but not 12:00am
    elif string[-2:] == 'am':
        # return the string from beginng up until 'am'
        return string[:-2]
    # if it's pm and starts with 12
    elif string[-2:] == 'pm' and string[:2] == '12':
        # return the string without pm
        return string[:-2]
    #otherwise
    else:
        # add twelve to the hour and return the :00 added to it 
        return str(int(string[:2]) + 12) + string[2:8]

twelveto24('04:45pm')
twelveto24('6:00am')
twelveto24('12:45pm')
twelveto24('10:30pm')



