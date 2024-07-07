import random

def R_P_S():
    print("Play Rock, Paper, scissors with computer")
    p=input("Enter Player Name: ")
    a=0
    p1=0
    c1=0
    
    
    while a!=5:
        print("1 for Rock")
        print("2 for Paper")
        print("3 for Scissors")
        print("4 to check score")
        print("5 to exit")
        try:
            a=int(input())
        except:
            continue
        r=random.randint(1, 3)
        if a==1:
            print("you choose Rock")
        elif a==2:
            print("You choose Paper")
        elif a==3:
            print("You choose Scissors")
        elif a==4:
            print("Your score: "+str(p1))
            print("Computer score: "+str(c1))
            continue
        elif a==5:
            print("Your score: "+str(p1))
            print("Computer score: "+str(c1))
            print("Thanks for playing")
            break
        else:
            print("Invalid option")
            continue
        
        if r==1:
            print("Computer choose Rock")
            if a==1:
                print("No one wins")
            elif a==2:
                print("You win")
                p1+=1
            else:
                print("Computer win")
                c1+=1
        elif r==2:
            print("Computer choose Paper")
            if a==2:
                print("No one wins")
            elif a==3:
                print("You win")
                p1+=1
            else:
                print("Computer win")
                c1+=1
        elif r==3:
            print("Computer choose Scissors")
            if a==3:
                print("No one wins")
            elif a==1:
                print("You win")
                p1+=1
            else:
                print("Computer win")
                c1+=1
    return 0

R_P_S()
    
    