# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())

print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())

print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

fruit_vowels = []
vowels = ['a','e','i','o','u']
for fruit in fruits:
    for char in fruit:
        if char in vowels:
            fruit_vowels.append(fruit)

fruits_with_more_than_two_vowels_raw = []
for fruit in fruit_vowels:
    if fruit_vowels.count(fruit) > 2:
        fruits_with_more_than_two_vowels_raw.append(fruit)


fruits_with_more_than_two_vowels = []
for fruit in fruits_with_more_than_two_vowels_raw:
    if fruit not in fruits_with_more_than_two_vowels:
        fruits_with_more_than_two_vowels.append(fruit)

print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']


fruit_vowels = []
vowels = ['a','e','i','o','u']
for fruit in fruits:
    for char in fruit:
        if char in vowels:
            fruit_vowels.append(fruit)

fruits_with_two_vowels_raw = []
for fruit in fruit_vowels:
    if fruit_vowels.count(fruit) == 2:
        fruits_with_two_vowels_raw.append(fruit)


fruits_with_two_vowels = []
for fruit in fruits_with_two_vowels_raw:
    if fruit not in fruits_with_two_vowels:
        fruits_with_two_vowels.append(fruit)

print(fruits_with_two_vowels)


# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_characters = []
for fruit in fruits:
    if len(fruit) > 5:
        fruits_with_more_than_five_characters.append(fruit)

fruits_with_more_than_five_characters
# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits_with_exactly_five_characters = []
for fruit in fruits:
    if len(fruit) == 5:
        fruits_with_exactly_five_characters.append(fruit)

fruits_with_exactly_five_characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_characters = []
for fruit in fruits:
    if len(fruit) < 5:
        fruits_with_less_than_five_characters.append(fruit)

fruits_with_less_than_five_characters
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
character_count = []
for fruit in fruits:
    character_count.append(len(fruit))

character_count
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = []
for fruit in fruits:
    if 'a' in fruit in fruits:
        fruits_with_letter_a.append(fruit)

fruits_with_letter_a
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

even_numbers
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)

odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = []
for n in numbers:
    if n > 0:
        positive_numbers.append(n)

positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = []
for n in numbers:
    if n < 0:
        negative_numbers.append(n)

negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_with_2_or_more_numbers = []
for n in numbers:
    if abs(n) > 9:
        numbers_with_2_or_more_numbers.append(n)

numbers_with_2_or_more_numbers

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = []
for n in numbers:
    numbers_squared.append(n**2)

numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = []
for n in numbers:
    if n < 0 and n % 2 != 0:
        odd_negative_numbers.append(n)

odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = []
for n in numbers:
    numbers_plus_5.append(n + 5)

numbers_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
