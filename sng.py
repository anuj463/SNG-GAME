 # python project to implement Snake-Water-Gun game 
 # Author: Anuj Savant
 # Date: 5/7/25
print("Menue:")
print("1-Snake\n2-Water\n3-Gun\n4-Exit")
player1=0
player2=0

while True :
    op1 = int(input("Enter 1st option:"))
    op2 = int(input("Enter 2nd option:"))

    if(op1==1 and op2==2):
       player1=player1+1
    elif(op1==1 and op2==3):
        player2=player2+1
    elif (op1==1 and op2==1):
        player1 = player1 + 0
        player2 = player2 + 0
    elif(op1==2 and op2==1):
        player1 = player1 + 1
    elif(op1==2 and op2==3):
        player = player1 + 1
    elif op1==2 and op2==2:
        player1 = player1 + 0
        player2 = player2 + 0
    elif op1==3 and op2==3:
        player1 = player1 + 0
        player2 = player2 + 0
    elif op1==1 and op2==3:
        player2 = player2 + 1
    elif op1==3 and op2==2:
         player2 = player2 + 1
    elif op1==3 and op2==1:
        player1 = player1 +1
    elif op1 == 4 and op2 == 4:
        print("Game Over")
        break



print("player1 score is:",player1)

print("player2 score is:",player2)

if player1 > player2:
    print("Player 1 wins!")
elif player1 == player2:
     print("Draw!")
else:
    print("Player 2 wins!")
    