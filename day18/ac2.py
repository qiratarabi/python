import random
playing = True
while playing:
    user_action = input("Enter a choice (rock, paper, scissors):")
    possible_actions = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(possible_actions)
    if user_action == 'paper' and computer_choice == 'scissor':
        print("User won")
    elif user_action == 'rock' and computer_choice == 'scissor':
        print("User won")
    elif user_action == 'paper' and computer_choice =='rock':
        print("User won")
    elif user_action == computer_choice:
        print("Draw")
    else:
        print("Computer won")
        