import random

computer_number = random.randint(1, 100)

print(computer_number)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print(f"Invalide input. Try again...")
        continue

    player_number = int(player_input)
    if player_number == computer_number:
        print(f"You guess it!")
        break

    elif player_number > computer_number:
        print(f"Too High!")

    elif player_number < computer_number:
        print(f"Too Low")


#----Finished
#----Test in Linux