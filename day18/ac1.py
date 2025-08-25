import random
playing = True
number = str(random.randit(10, 20))
print("I will generate a number between 10 to 20 and you have to guess")
print("The game ends when you get the number")
while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("You win")
        break
    else:
        print("Wrong guess")