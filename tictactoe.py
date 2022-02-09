def play():#Board
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    #Print Empty Board
    print("   0  1  2")
    count = 0        
    for row in game:
        print(count,row)    
        count = count+1
    turn = 0 #Turn Number at Start

    while (turn < 9): #Alternating Turns
        #Player 1:
        if (turn % 2) == 0:
            print("Player 1's Turn:")

            while True: #Non Number Input
                try:
                    a = int(input(" Enter Row:"))
                    b = int(input(" Enter Column:"))
                    break #Breaks out of loop if ValueError is (a,b>2)
                except ValueError:
                    print(" --Input must be 0,1 or 2--")
                    continue

            while a>2 or b>2: #Input Out of Range
                try:
                    print(" --Input must be 0,1 or 2--")
                    a = int(input(" Retry Row:"))
                    b = int(input(" Retry Column:"))
                except ValueError:
                    print(" --Input must be 0,1 or 2--")
                    continue
                
            while game[a][b] != 0: #If Space is Occupied
                try:
                    print(" --Space is Taken--")
                    a = int(input(" Retry Row:"))
                    b = int(input(" Retry Column:"))
                    while a>2 or b>2: #If After Space Taken an invalid input is given (a,b>2) it asks user again
                        
                        try:
                            print(" --Input must be 0,1 or 2--")
                            a = int(input(" Retry Row:"))
                            b = int(input(" Retry Column:"))
                        except ValueError: #After giving invalid input (a,b>2). Giving another (a,b>2) or (letter..) asks user again
                            print(" --Input must be 0,1 or 2--")
                            continue

                except ValueError: #If After Space Taken a non-number is given asks user again
                    print(" --Input must be 0,1 or 2--")
                    continue
                
            if game[a][b] == 0: #Player 1 Places
                game[a][b] = 1
        #Player 2
        else:
            print("Player 2's Turn:")

            while True: #Non Number Input
                try:
                    a = int(input(" Enter Row:"))
                    b = int(input(" Enter Column:"))
                    break
                except ValueError:
                    print(" --Input must be 0,1 or 2--")
                    continue

            while a>2 or b>2: 
                try:
                    print(" --Input must be 0,1 or 2--")
                    a = int(input(" Retry Row:"))
                    b = int(input(" Retry Column:"))
                except:
                    print(" --Input must be 0,1 or 2--")
                    continue

            while game[a][b] != 0: #If Space is Occupied
                try:
                    print(" --Space is Taken--")
                    a = int(input(" Retry Row:"))
                    b = int(input(" Retry Column:"))
                    while a>2 or b>2: #If After Space Taken an invalid input is given (a,b>2) it asks user again

                        try:
                            print(" --Input must be 0,1 or 2--")
                            a = int(input(" Retry Row:"))
                            b = int(input(" Retry Column:"))
                        except ValueError: #After giving invalid input (a,b>2). Giving another (a,b>2) or (letter..) asks user again
                            print(" --Input must be 0,1 or 2--")
                            continue

                except:
                    print(" --Input must be 0,1 or 2--")
                    continue

            if game[a][b] == 0: #Player 2 Places
                game[a][b] = 2

        #Print Board After Each Turn       
        print("   0  1  2")
        count = 0
        for row in game:
            print(count, row)
            count = count + 1
        turn = turn+1 #Turn Number After Each Turn

        def win(p):#Horizontal,Vertical,Diagonal Win Conditions
            if game[a][0] == p and game[a][1] == p and game[a][2] == p\
            or game[0][b] == p and game[1][b] == p and game[2][b] == p\
            or game[1][1] == p and game[0][0] == p and game[2][2] == p\
            or game[1][1] == p and game[2][0] == p and game[0][2] == p:
                return 1

        if win(p=1)==1: #Win
            print(" --Player 1 Wins--")
            turn = turn+(9-turn) #Reset Board
        if win(p=2)==1:
            print(" --Player 2 Wins--")
            turn = turn+(9-turn) #Reset Board

def structure(): #Structure of Events
    while True:
        try:
            x = input(
"""Enter 1 for New Game 
Enter 2 for Exit""")
            if int(x)==1:
                play()
            if int(x)==2:
                break
        except:
            print(" --Input must be 0,1 or 2--")
print("v1") #Version Testing 

structure() #The Program

"""All Input Errors fixed, shorten code"""


