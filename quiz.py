questions =("Whats the highest runs scored in an ipl edition",
            "Which player won the most purple caps in ipl",
            "Who is the youngest player ever to play ipl",
            "Who is the most successful captain in ipl",
            "Which is the only team that won all three qualifying games to win a trophy in ipl")

options = (("A.Virat Kohli","B.Chris Gayle","C.David Warner","D.Jos Butler"),
           ("A.Bumrah","B.Lasith Malinga","C.Bhuvaneshwar Kumar","D.Yuzvendra Chahal"),
           ("A.Riyan Parag","B.Vaibhav Sooryavanshi","C.Paras Ray Barman","D.Ishan Kishan"),
           ("A.Rohit Sharma","B.MS Dhoni","C.Gautam Gambhir","D.David Warner"),
           ("A.CSK","B.RCB","C.MI","D.SRH"))

guesses = []
q_num = 0
score = 0
answers = ("A","C","B","A","D")
for q in questions :
    print("---------------------------------")
    print(q)
    for op in options[q_num] :
        print(op)
        
    guess = input("Enter (A,B,C,D) :").upper()
    guesses.append(guess)
    if guess == answers[q_num] :
        print("CORRECT !")
        score += 1
    else :
        print("INCORRECT!")
        print(f"The CORRECT answer is {answers[q_num]}")
    q_num += 1

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

