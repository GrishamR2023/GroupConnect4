import random
class Turn:
    def __init__(self):
        pass        
        
        
        

    def move(self,positions,currentPlayer):
        turnOver = False
        while turnOver == False:
            ui = input(f"What column would you like to play? ({currentPlayer}) : ")
            if not(ui.isdigit):
                print("please enter a number...")
            elif len(ui) > 1:
                print("please enter a single digit number...")
            elif ui.isdigit():
                    x = int(ui)-1
                    for i in range(0,7,1):
                        y = i
                        if positions[y][x] == " ":
                            positions[y][x] = currentPlayer
                            print(positions)
                            return positions
                        else:
                            print("Help")
                            y+=1 


    def computer(self,positions,currentPlayer):
        turnOver = False
        while turnOver == False:
            x = random.randint(0,6)
            for i in range(0,7,1):
                y = i
                if positions[y][x] == " ":
                    positions[y][x] = currentPlayer
                    print(positions)
                    return positions
                else:
                    print("Help")
                    y+=1 


                        
                        
    def check(self,positions,player1):
        x = 0
        y = 0
        #Horizontal check L->R
        for a in range(0,6,1):
            for i in range(0,3,1):
                if positions[y][x] == player1 and positions[y][x+1] == player1 and positions[y][x+2] == player1 and positions[y][x+3] == player1:
                    winner = player1
                    return winner
                x+=1
            x = 0
            y+=1
        x = 0
        y = 0
        #Horizontal check R->L
        for a in range(0,6,1):
            for i in range(0,3,1):
                if positions[y][x-1] == player1 and positions[y][x-2] == player1 and positions[y][x-3] == player1 and positions[y][x-4] == player1:
                    winner = player1
                    return winner
                x+=1
            x = 0
            y+=1
        x = 0
        y = 0
        #Vertical check 
        for a in range(0,3,1):
            for i in range(0,7,1):
                if positions[y][x] == player1 and positions[y+1][x] == player1 and positions[y+2][x] == player1 and positions[y+3][x] == player1:
                    winner = player1
                    return winner
                x+=1
            x = 0
            y+=1
        #Diagonal check L->R
        x=0
        y=0
        for a in range(0,3,1):
            for i in range(0,3,1):
                if positions[y+3][x] == player1 and positions[y+2][x+1] == player1 and positions[y+1][x+2] == player1 and positions[y][x+3] == player1:
                    winner = player1
                    return winner
                x+=1
            y+=1
            x=0
        #Diagonal check R->L
        x=0
        y=0
        for a in range(0,3,1):
            for i in range(0,3,1):
                if positions[y][x] == player1 and positions[y+1][x+1] == player1 and positions[y+2][x+2] == player1 and positions[y+3][x+3] == player1:
                    winner = player1
                    return winner
                x+=1
            y+=1
            x=0
        x = 0
        y = 0
        winner = False
        return winner