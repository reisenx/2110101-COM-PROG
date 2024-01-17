#Input reqiured score and setup initial score to 0
win_score = int(input())
player1_score = 0
player2_score = 0

#Input game and count a score for thrice of require score times

for i in range(0,3*win_score+1):
    #In the first 3n loop, input the game, count the score and declared the result if someone winning during the process
    if(i in range(0,3*win_score)):
        if(player1_score != win_score and player2_score != win_score):
            #Input a string in each line (Ex. "R P")
            game = str(input())
            #Split it to a list (Ex. "R P" --> ["R", "P"])
            RSP = game.split()

            #Count the score
            #Index 0 of the list is player 1 and Index 1 of the list is player 2
            #If win, add the winner score by 1
            #Scissors (S) wins Paper (P)
            if(RSP[0]=='S' and RSP[1]=='P'):
                player1_score = player1_score + 1
            elif(RSP[1]=='S' and RSP[0]=='P'):
                player2_score = player2_score + 1
            #Paper (P) wins Rock (R)
            elif(RSP[0]=='P' and RSP[1]=='R'):
                player1_score = player1_score + 1
            elif(RSP[1]=='P' and RSP[0]=='R'):
                player2_score = player2_score + 1
            #Rock (R) wins Scissors (S)
            elif(RSP[0]=='R' and RSP[1]=='S'):
                player1_score = player1_score + 1
            elif(RSP[1]=='R' and RSP[0]=='S'):
                player2_score = player2_score + 1
            #Else, do not count the score (Tie)
            else:
                pass
    
        #In case that player 1 have reached the required score
        elif(player1_score == win_score):
            print("Player 1 wins")
            break
    
        #In case that player 2 have reached the required score
        elif(player2_score == win_score):
            print(player1_score, player2_score)
            print("Player 2 wins")
            break

    #Last loop (3n+1 loop) just check the result in case you just win, lose or tie in the last game
    else:
        if(player1_score != win_score and player2_score != win_score):
            print(player1_score, player2_score)
            print("Tie")
        elif(player1_score == win_score):
            print(player1_score, player2_score)
            print("Player 1 wins")
        elif(player2_score == win_score):
            print(player1_score, player2_score)
            print("Player 2 wins")