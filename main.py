import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total=nr_letters+nr_symbols+nr_numbers
password=""
final=""
for n in range(0,nr_letters):
    password+=letters[random.randint(1,len(letters))-1]+","
for n in range(0,nr_numbers):
    password+=numbers[random.randint(1,len(numbers))-1]+","
for n in range(0,nr_symbols):
    password+=symbols[random.randint(1,len(symbols))-1]+","
password=password.split(",")
for n in range(0,total):
    rnd=random.randint(1,total)-1
    rnd2=random.randint(1,total)-1
    temp=password[rnd]
    password[rnd]=password[rnd2]
    password[rnd2]=temp
for letter in password:
    final+=letter
print(f"Your password id {final}")
