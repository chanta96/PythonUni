from random import randrange
number_to_guess = randrange(1,100)
user_number = int(input("ingrese su numero:"))
while user_number != number_to_guess:
    if user_number > number_to_guess:
        print("muy alto, proba uno menor")
    else:
        print("muy bajo, proba uno mayor")
    user_number = int(input("ingresa otro numero:"))
else:
    print('felicidades')
