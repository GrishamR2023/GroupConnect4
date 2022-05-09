import turtle as t
import os
import PVP
#varibles
#Screens
mainScreen = t.Screen()
mainScreen.screensize(canvheight=400,canvwidth=200)
#Turtles
PvC = t.Turtle()
PvP = t.Turtle()
Directions = t.Turtle()
Credits = t.Turtle()
#lists
wordingList=["PvC","PvP","Directions","Credits"]
numsList=[240,95,-65,-210]
turtles=[PvC,PvP,Directions,Credits]
#Functions
def setup():
    #Turtle Config
    for i in turtles:
        i.shapesize(2)
        i.shape("square")
        i.speed(0)
        i.color("blue")
        i.penup()
    t.penup()
    t.goto(0,240)
    t.hideturtle()
    #Positions
    PvC.goto(0,225)
    PvP.goto(0,80)
    Directions.goto(0,-80)
    Credits.goto(0,-225)
    for i in range(4):
        j = numsList[i]
        k = wordingList[i]
        t.goto(0,j)
        t.write(arg=f"{k}",move=True, align="center", font=("Arial", 24, "normal"))
def pvc(x,y):
    print("pvc")
    mainScreen.update()
def pvp(x,y):
    pass
def directions(x,y):
    print("directions")
    mainScreen.update()
def credits(x,y):
    mainScreen.reset()
    t.penup()
    t.hideturtle()
    Credits.hideturtle()
    Directions.hideturtle()
    PvC.hideturtle()
    PvP.hideturtle()
    Credits.penup
    Credits.goto(0,0)
    Credits.write(arg=f"Credits",move=True, align="center", font=("Arial", 24, "normal"))
    Credits.goto(0,-60)
    Credits.write("\tAdam -- User Interface\n" "Rece -- Back End, Game User Interface",move=True, align="center", font=("Arial", 24, "normal"))
setup()
PvC.onclick(pvc)
PvP.onclick(pvp)
Directions.onclick(directions)
Credits.onclick(credits)
mainScreen.mainloop()