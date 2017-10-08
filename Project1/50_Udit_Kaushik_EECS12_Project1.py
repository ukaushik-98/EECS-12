#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#################################

import turtle

def draw_shape(n):
    print("Click the graphics screen to exit out")
    window = turtle.Screen()
    window.bgcolor("light blue")
    shape = turtle.Turtle()
    angle = 360 / n
    if n <10:
        length = 150
    else:
        length = 50
    for i in range(n):
        shape.forward(length)
        shape.left(angle)
    window.exitonclick()

def shape():
    infile = open("shapes.txt", "r")
    x = infile.readlines()
    print("Welcome to the Shapes Function!\nPlease enter a number between 3 through 20.")
    while True:
        user_input = int(input("Please enter the number of sides: "))
        shape_list = ["Triangle", "Square", "Pentagon", "Hexagon","Septagon", "Octagon"]
        if user_input < 3 or user_input > 20:
            print("Not in range (3-20)")
        else:
            print(x[user_input - 3])
            draw_shape(user_input)
            break
shape()
