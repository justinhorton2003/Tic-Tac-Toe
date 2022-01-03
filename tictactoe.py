def play():#Board
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    print("   0  1  2")
    count = 0        
    for row in game:
        print(count,row)    
        count = count+1
    turn = 0
    while (turn < 9):
        #Player 1:
        if (turn % 2) == 0:
            print("Player 1's Turn:")
            a = int(input(" Enter Row:"))
            b = int(input(" Enter Column:"))
            while game[a][b] != 0:
                print("-Space is Taken-")
                a = int(input(" Retry Row:"))
                b = int(input(" Retry Column:"))
            if game[a][b] == 0:
                game[a][b] = 1
        #Player 2
        else:
            print("Player 2's Turn:")
            a = int(input(" Enter Row:"))
            b = int(input(" Enter Column:"))
            while game[a][b] != 0:
                print("-Space is Taken-")
                a = int(input(" Retry Row:"))
                b = int(input(" Retry Column:"))
            if game[a][b] == 0:
                game[a][b] = 2
        print("   0  1  2")#Board Numbering
        count = 0
        for row in game:
            print(count, row)
            count = count + 1
        turn = turn+1
        def win():#Horizontal,Vertical,Diagonal Conditions
            if game[a][0] == 1 and game[a][1] == 1 and game[a][2] == 1\
            or game[0][b] == 1 and game[1][b] == 1 and game[2][b] == 1\
            or game[1][1] == 1 and game[0][0] == 1 and game[2][2] == 1\
            or game[1][1] == 1 and game[2][0] == 1 and game[0][2] == 1:
                print("Player 1 Wins");return 1
            if game[a][0] == 2 and game[a][1] == 2 and game[a][2] == 2\
            or game[0][b] == 2 and game[1][b] == 2 and game[2][b] == 2\
            or game[1][1] == 2 and game[0][0] == 2 and game[2][2] == 2\
            or game[1][1] == 2 and game[2][0] == 2 and game[0][2] == 2:
                print("Player 2 Wins");return 1
        if win()==1:
            turn = turn+(9-turn) #Reset Board
while True:
    x = int(input("""
Enter 1 for New Game 
Enter 2 for Exit"""))
    if x==1:
        play()
    if x==2:
        break

