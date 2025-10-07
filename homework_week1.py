# Bootcamp Homework - Week 1

# 1. Count vowels in a word
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print(f"The number of vowels in '{word}' is {count}.")


# 2. Print animals in all caps
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())


# 3. Print numbers 1–20, marking odd/even
for number in range(1, 21):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


# 4. Palindrome check
text = input("Enter a word or phrase: ").lower().replace(" ", "")
if text == text[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


# 5. Sum of two integers
def sum_of_integers(a, b):
    return a + b

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("The sum is:", sum_of_integers(num1, num2))
