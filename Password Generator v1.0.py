
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
sum=nr_letters+nr_symbols+nr_numbers
list=[]
password=""


for char in range(1,nr_letters+1):
    char=None
    letter=random.choice(letters)
    list.append(letter)
for char in range(1,nr_numbers+1):
    char=None
    number=random.choice(numbers)
    list.append(number)
for char in range(1,nr_symbols+1):
    char=None
    symbol=random.choice(symbols)
    list.append(symbol)
for char in range(0,sum):
    char=None
    password+=random.choice(list)
print(f"{sum} haneli şifreniz {password}")
exit()
