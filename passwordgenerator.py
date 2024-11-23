import random

print("Welcome to Password Generator !")

chars = "nehadhawassureshvarshatushar1234567890!@#$%^&*()"

number = input('Enter number of password you want:')
number = int(number)

length = input('Enter the lenght of your willing passowrd:')
length = int(length)

print("\n Your new Password is:")

for passd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)

  print(password)