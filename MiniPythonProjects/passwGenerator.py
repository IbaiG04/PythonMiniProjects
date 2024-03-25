import random

print ("Welcome to the Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*.,?0123456789'

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

print('\nYour passwords are:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    