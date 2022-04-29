from Turn import Turn
#Variables



player1 = "O"
player2 = "X"
end = False
currentTurn = 0
winner = False
layer1 = [" "," "," "," "," "," "," "]
layer2 = [" "," "," "," "," "," "," "]
layer3 = [" "," "," "," "," "," "," "]
layer4 = [" "," "," "," "," "," "," "]
layer5 = [" "," "," "," "," "," "," "]
layer6 = [" "," "," "," "," "," "," "]
layer7 = [" "," "," "," "," "," "," "]
positions = [layer1,layer2,layer3,layer4,layer5,layer6,layer7]
board = (f"""
     1         2         3         4         5         6         7
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[0][0]}   | |   {positions[0][1]}   | |   {positions[0][2]}   | |   {positions[0][3]}   | |   {positions[0][4]}   | |   {positions[0][5]}   | |   {positions[0][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[1][0]}   | |   {positions[1][1]}   | |   {positions[1][2]}   | |   {positions[1][3]}   | |   {positions[1][4]}   | |   {positions[1][5]}   | |   {positions[1][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[2][0]}   | |   {positions[2][1]}   | |   {positions[2][2]}   | |   {positions[2][3]}   | |   {positions[2][4]}   | |   {positions[2][5]}   | |   {positions[2][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[3][0]}   | |   {positions[3][1]}   | |   {positions[3][2]}   | |   {positions[3][3]}   | |   {positions[3][4]}   | |   {positions[3][5]}   | |   {positions[3][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[4][0]}   | |   {positions[4][1]}   | |   {positions[4][2]}   | |   {positions[4][3]}   | |   {positions[4][4]}   | |   {positions[4][5]}   | |   {positions[4][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[5][0]}   | |   {positions[5][1]}   | |   {positions[5][2]}   | |   {positions[5][3]}   | |   {positions[5][4]}   | |   {positions[5][5]}   | |   {positions[5][6]}   |
  -------   -------   -------   -------   -------   -------   -------""")
#Functions



            
#Main game loop
print(board)
while end == False:
    currentTurn = 0
    for i in range(0,2,1):
        if currentTurn == 0:
            t = Turn()
            positions = t.move(positions,"O")
        elif currentTurn == 1:
            t = Turn()
            positions = t.move(positions,"X")
        board = (f"""
     1         2         3         4         5         6         7
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[5][0]}   | |   {positions[5][1]}   | |   {positions[5][2]}   | |   {positions[5][3]}   | |   {positions[5][4]}   | |   {positions[5][5]}   | |   {positions[5][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[4][0]}   | |   {positions[4][1]}   | |   {positions[4][2]}   | |   {positions[4][3]}   | |   {positions[4][4]}   | |   {positions[4][5]}   | |   {positions[4][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[3][0]}   | |   {positions[3][1]}   | |   {positions[3][2]}   | |   {positions[3][3]}   | |   {positions[3][4]}   | |   {positions[3][5]}   | |   {positions[3][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[2][0]}   | |   {positions[2][1]}   | |   {positions[2][2]}   | |   {positions[2][3]}   | |   {positions[2][4]}   | |   {positions[2][5]}   | |   {positions[2][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[1][0]}   | |   {positions[1][1]}   | |   {positions[1][2]}   | |   {positions[1][3]}   | |   {positions[1][4]}   | |   {positions[1][5]}   | |   {positions[1][6]}   |
  -------   -------   -------   -------   -------   -------   -------
 |   {positions[0][0]}   | |   {positions[0][1]}   | |   {positions[0][2]}   | |   {positions[0][3]}   | |   {positions[0][4]}   | |   {positions[0][5]}   | |   {positions[0][6]}   |
  -------   -------   -------   -------   -------   -------   -------""")            
        print(board)
        winner = t.check(positions,"X")
        winner = t.check(positions,"O")
        if winner != False:
            end = True
            print(winner)
            break
        currentTurn = 1
