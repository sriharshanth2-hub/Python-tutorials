import random
low = 1
high = 100
guesses = 0
y = random.randint(low,high)
while True :
    x = int(input("ENTER A NUMBER BETWEEN 1-100 : "))
    if x < 1 or x > 100 :
        print("Please enter a number in between 1-100")
    if x < y :
        print("Lower than Desired number")
        guesses += 1
    if x > y :
        print("Higher than Desired number")
        guesses += 1
    if x == y :
        print("You are CORRECT!!")
        guesses += 1
        break
print(f"You took {guesses} guesses to get correct number")


