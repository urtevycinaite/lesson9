# squares = []
# for number in range(10):
#     if number != 5:
#         squares.append(number * number)
# print(squares)

# squares = [number * number for number in range(10) if number != 5]
# print(squares)

# squares = []
# for number in range(10):
#     if number % 2 == 0:
#         squares.append(number * number)
# print(squares)

# names = ["Albert", "Alma", "Joseph", "Zoe"]
# names_with_a = []

# for name in names:
#     if name.startswith("A"):
#         names_with_a.append(name)

# print(names_with_a)


# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A") or "e" in name])



# squares = [number * number for number in range(10) if number % 2 == 0]
# print(squares)

# 1. Find all of the numbers from 1-1000 that are divisible by 6.

# numbers = [number for number in range(1000) if number % 6 == 0]
# print(numbers)

# 2. Find all number from 1-1000 that have 9 in them.

# numbers_with_nine = [number for number in range(1000) if "9" in str(number)]

# # print("Numbers from 1 to 100 that have '9' in them:")
# print(numbers_with_nine)

# squares = {i: i * i for i in range(10) if i !=5}
# print(squares)

# squares = {i: i * i for i in range(10) if i % 2 !=0}
# print(squares)

# values = ["a", "b", "c"]

# for value in values:
#     print(value)
    
# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)


# values = ["a", "b", "c"]
# for value in enumerate(values):
#     print(value)
#     index, value = value
#     print(f"after unpacking: {index}, {value}")

# values = ["a", "b", "c"]
# for count, value in enumerate(values, start=1):
#     print(count, value)

# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if i % 2==0]

# seq = list(range(15, 21))

# print(even_items(seq))

# import math

# arae = 5 * 5 * math.pi
# print(math.factorial(9))

# 3. Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.

# text = "In this lecture we will review some additional functionalities of python built-in data structures."

# words = text.split()

# words_with_e = [word for word in words if "e" in word]
# count_words_with_e = len(words_with_e)

# print(count_words_with_e)

    
# 4. Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.

# text = "In this lecture we will review some additional functionalities of python built-in data structures."

# words = text.split()

# more_than_five_characters = [word for word in words if len(word) >5]
# count = len(more_than_five_characters)

# print(count)

# 5. Write a program that checks if given number is a perfect square.

# import math

# def perfect_square(number):
#     square = math.isqrt(number)
#     return square * square == number
# number = int(input("Enter a number: "))
# if perfect_square(number):
#     print("It's a perfcet square!")
# else:
#     print("It's not a perfect match!")

