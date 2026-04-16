import random

options = ("rock", "paper", "scissors")
wins = 0
losses = 0
ties = 0

playing = True

while playing:
    player = input("Enter choice (rock, paper, scissors): ").lower()

    if player not in options:
        print("Invalid choice!")
        continue

    computer = random.choice(options)

    print(f"Computer = {computer}")
    print(f"Player = {player}")

    if player == computer:
        print("It's a tie")
        ties += 1

    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
        wins += 1

    else:
        print("You lose!")
        losses += 1

    choice = input("Play again? (yes/no): ").lower()
    if choice != "yes":
        playing = False

print("\nFinal Score:")
print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")