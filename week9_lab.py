import turtle
import os 
import sys
t = turtle.Turtle()

# # draw a single triangle
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)

t.speed(0) 

def draw_triangle(level):

    def recursive_walk(level):
        if level > 0:
            recursive_walk(level -1)
            t.left(60)
            recursive_walk(level -1)
            t.right(120)   
            recursive_walk(level -1)
            t.left(60)
            recursive_walk(level -1)
        else:
            t.forward(3)

    for i in range(3):
        recursive_walk(level)
        t.right(120)

draw_triangle(4)

turtle.exitonclick()


'''
expected:
forward
left 60
forward
right 120
forward
left 60
forward
left 60





'''