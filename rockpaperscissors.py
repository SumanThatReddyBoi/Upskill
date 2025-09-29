import random

print("Welcome! To quit press 'Q'")
print("Rock - 'R', Paper - 'P', Scissors - 'S'")

user = 0
computer = 0
u = 0
c = 0

while(1):
    print("Rock...Paper...Scissors...")
    gen = random.randint(1, 3)
    if gen == 1:
        gen_rps = 'R'
        action = "Rock"
    elif gen == 2:
        gen_rps = 'P'
        action = "Paper"
    elif gen == 3:
        gen_rps = 'S'
        action = "Scissors"
        
    rps = input()
    out2 = print("Computer Played: " + action)

    if(rps == 'R'):
        if(gen_rps=='R'):
            print("Tie!")
        elif(gen_rps=='P'):
            print("Computer Wins!")
            c = 1
        elif(gen_rps=='S'):
            print("You Win!")
            u = 1
    
    elif(rps == 'P'):
        if(gen_rps=='R'):
            print("You Win!")
            u = 1
        elif(gen_rps=='P'):
            print("Tie!")
        elif(gen_rps=='S'):
            print("Computer Wins!")
            c = 1
    
    elif(rps == 'S'):
        if(gen_rps=='R'):
            print("Computer Wins!")
            c = 1
        elif(gen_rps=='P'):
            print("You Win!")
            u = 1
        elif(gen_rps=='S'):
            print("Tie!")
    
    elif(rps == 'Q'):
        break
    
    else:
        print("Invalid Charecter Entered!")

    if c == 1:
        computer = computer + 1
    elif u == 1:
        user = user + 1
    
    c = 0
    u = 0

    if(computer > user):
        print("Computer is Winning!")
        print(computer, " - ", user)
    elif(computer < user):
        print("You are Winning!")
        print(computer, " - ", user)
    elif(computer == user):
        print("You are currently tied!")
        print(computer, " - ", user)

    print()
    print()