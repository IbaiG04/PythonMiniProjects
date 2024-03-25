import random
numerSecreto = random.randint(1, 20)

numero=input("I am thinking of a number between 1 and 20.")
numero=int(numero)
intentos = 0
while numero != numerSecreto and intentos < 6:
    if numero < numerSecreto:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is too high.")
    numero = input("Try again:")
    numero = int(numero)
    intentos += 1
if numero == numerSecreto:
    print(f"Good job! You guessed the number in {intentos} tries!")
