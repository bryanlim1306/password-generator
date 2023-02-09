#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_letters = []
pw_symbols = []
pw_numbers = []
password = ""

for i in range(nr_letters):
  chosen_letter = letters[random.randint(0, len(letters)-1)]
  pw_letters.append(chosen_letter)

for i in range(nr_symbols):
  chosen_symbol = symbols[random.randint(0, len(symbols)-1)]
  pw_symbols.append(chosen_symbol)

for i in range(nr_numbers):
  chosen_number = numbers[random.randint(0, len(numbers)-1)]
  pw_numbers.append(chosen_number)

combine_chosen = pw_letters + pw_symbols + pw_numbers
random.shuffle(combine_chosen)
for e in combine_chosen:
  password += e

print(f"Your generated password is: {password}")