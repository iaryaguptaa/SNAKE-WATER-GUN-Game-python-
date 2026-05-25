import random

def game_win(user, computer):
    if user==computer:
        return None
    
    #SNAKE VS WATER
    if user =="s" and computer =="w":
        return True
    if user =="w" and computer =="s":
        return False
    
    #WATER VS GUN
    if user =="w" and computer =="g":
        return True
    if user =="g" and computer =="w":
        return False
    
    # GUN VS SNAKE
    if user =="g" and computer =="s":
        return True
    if user =="s" and computer =="g":
        return False
    
rand_no = random.randint(1,3)

print("Computer's turn: Snake(s), Water(w), Gun(g)")
if rand_no ==1:
    computer = "s"
elif rand_no ==2:
    computer = "w"
else:
    computer = "g"

user = input("Your turn: Snake(s), Water(w), Gun(g)").lower()

result = game_win(user, computer) #RETURNS TRUE IF YOU WIN, FALSE FOR LOSE, NONE FOR DRAW
print(f"\nYou chose:{user}")
print(f"\nComputer chose:{computer}")

if result is None:
    print("Its a draw!")

elif(result):
    print("Yow win!")
else:
    print("You lose!")