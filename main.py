"""
This is a Password Generator code based on letters, numbers and some symbols
"""
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(number_of_letters, number_of_numbers, number_of_symbols):
    """
    This function returns a password based on letters, numbers and symbols
    """
    my_password = []
    for _ in range(1, number_of_letters + 1):
        my_password += random.choice(letters)

    for _ in range(1, number_of_numbers + 1):
        my_password += random.choice(numbers)

    for _ in range(1, number_of_symbols + 1):
        my_password += random.choice(symbols)

    random.shuffle(my_password)
    password = "".join(my_password)

    return password


print("Welcome to the PyPassword Generator!\n")

input_letters = int(input("How many letters would you like in your password?\n"))
input_symbols = int(input("How many symbols?\n"))
input_numbers = int(input("How many numbers?\n"))

GENERATED_PASSWORD = generate_password(input_letters, input_numbers, input_symbols)
print(f"Your password is {GENERATED_PASSWORD}")
