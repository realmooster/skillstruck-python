both = input("Enter the plays: ").split("@")
player_a = both[0].split(" ")
player_b = both[1].split(" ")
#Code that separates the players after "@"
player_aScores = 0
player_bScores = 0
#Total scores for to calculate at the end

def game():
    global player_a 
    global player_aScores
    global player_b
    global player_bScores
    global placeholder
    for i in range(3):
        #Checks through the values 3 times through index 1, 2, 3
        if player_a[i] == player_b[i]:
            player_aScores and player_bScores + 0
        elif player_a[i] == "rock" and player_b[i] == "scissors":
            player_aScores += 1
        elif player_a[i] == "scissors" and player_b[i] == "paper":
            player_aScores += 1
        elif player_a[i] == "paper" and player_b[i] == "rock":
            player_aScores += 1
        elif player_b[i] == "rock" and player_a[i] == "scissors":
            player_bScores += 1
        elif player_b[i] == "scissors" and player_a[i] == "paper":
            player_bScores += 1
        elif player_b[i] == "paper" and player_a[i] == "rock":
            player_bScores += 1

    if player_aScores == player_bScores:
        print("Score of player a:",player_aScores, "Score of player b:",player_bScores,"Tie!")

    elif player_aScores > player_bScores:
        print("Score of player a:",player_aScores, "Score of player b:",player_bScores,"Player a won!")

    elif player_bScores > player_aScores:
        print("Score of player a:",player_aScores, "Score of player b:",player_bScores,"Player b won!")

game()


