import random
'''
1 for Stone
-1 for Paper
0 for Scissors


'''

computer=random.choice([-1,0,1])
youstr = (input("enter your choice: "))
youDict ={"s":1,
        "p":-1,
        "c":0}

reverseDict={1:"Stone",-1:"Paper",0:"Scissors"}

if youstr not in youDict:
    print("invalid choice! please choose 's' 'p' or 'c'.")
else:
    you = youDict[youstr]


    if(computer==you):
        print("Its draw")
    else:    
        if(computer ==-1 and you==1):
            print("You win!\u2665")


        elif(computer==-1 and you==0):
            print("You lose!")
            
        elif(computer==1 and you==-1):
            print("You lose!")
            
        elif(computer==1 and you==0):
            print("You win!\u2665")
            
        elif(computer==0 and you==-1):
            print("You win!\u2665")
            
        elif(computer==0 and you==1):
            print("You lose!")
        else:
            print("something went wrong")

print(f"You choose: {reverseDict[you]}\nComputer choose: {reverseDict[computer]}")