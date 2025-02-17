import random 
def check(com,user_input):
    if com == user_input:
        return 0

    if (com == 2 and user_input == 0 ):
        return -1
    if (com == 0 and user_input == 1 ):
        return -1
    if (com == 1 and user_input == 2 ):
        return -1
    return 1
com=random.randint(0,2)
print("what you want to chose :- (0)snake (1)water (2)gun")
user_input=int(input("enter your choice:"))

score = check(com,user_input)
print("your option is:",user_input)
print("computer option is:",com)
if (score == 0):
    print("tie")
elif (score == -1):
    print("You lose")
else:
    print("you win")