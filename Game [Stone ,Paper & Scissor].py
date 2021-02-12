                                           # WELCOME TO THE GAME #


import random
def game(comp,you):

    if comp==you:
        return None
    elif comp=='Sc':
        if you=='p':
            return False
        elif you=='St':
            return True

    elif comp=='P':
        if you=='st':
            return False
        elif you=='Sc':
            return True

    elif comp=='St':
        if you=='Sc':
            return False
        elif you=='p':
            return True

print("computer's turn:")

VaryNo=random.randint(1,3)
if VaryNo==1:
    comp='Sc'
elif VaryNo==2:
    comp='P'
elif VaryNo==3:
    comp='St'
print("Computer selected his choise...")

print("Now its Your's turn:")
print("For scissor press = Sc")
print("For Stone press = St")
print("For Paper press= P")
you=input("your selection:")

a=game(comp,you)
print(f"computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print('The game is tie!')
elif a:
    print("you win the game!")
else:
    print("You Lose!")

print("THANK YOU...!")

                                          #CREATED BY YASIN #