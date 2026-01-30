import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(100)
""" for i in range(4)
    t.forward(100)
    t.left(90)
     """
""" rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
""" 
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(60) """
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
addSquares(60) """
""" 
""" rotate = 90
def triangle(x,y):
    for i in range(3):
        t.forward(x)
        t.left(y)
"""  """
def addTriangles(iRange):
    length = 5
    for i in range(iRange):
        triangle(length, 144)
        length += 5
        t.right(5)
addTriangles(60)
"""  """
turtle.done() """