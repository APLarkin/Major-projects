from tkinter import *
from tkinter.messagebox import showinfo
from random import choice
from sys import exit

num_rows = 30
num_cols = 30
size = 15
speed = 35
grow_by_this_much = 4
snake = [(5,5), (4,5)]
direction = 'Right'

def get_new_spot():
    return choice([(x,y) for x in range(num_cols) for y in range(num_rows)
                   if (x,y) not in snake])
	
def callback(e):
    global direction
    if e.keysym in ['Up', 'Left', 'Down', 'Right']:
        direction = e.keysym

def redraw():
    canvas.delete(ALL)
    for x,y in snake:
        canvas.create_rectangle(x*size+1,y*size+1,(x+1)*size,(y+1)*size, fill='blue')    
    x,y = spot
    canvas.create_rectangle(x*size+1,y*size+1,(x+1)*size,(y+1)*size, fill='red')

def move():
    global snake, spot, growing_counter

    if snake[0] == spot:
        growing_counter += grow_by_this_much
        spot = get_new_spot()

    x,y = snake[0]

    if direction == 'Left':
        x -= 1
    elif direction == 'Right':
        x += 1
    elif direction == 'Up':
        y -= 1
    else:
        y += 1

    if (x,y) in snake or x==-1 or y==-1 or x==num_cols or y==num_rows:
        showinfo(title='Loser', message='You lost.  Bye!')
        root.destroy()
        exit()
    
    snake.insert(0, (x,y))

    if growing_counter == 0:
        snake = snake[:-1]
    else:
        growing_counter -= 1
    redraw()
    root.after(speed, move)

growing_counter = 0
spot = get_new_spot()

root = Tk()
canvas = Canvas(width=size*num_rows, height=size*num_cols, bg='white')
canvas.grid()
root.bind("<Key>", callback)
move()

mainloop()
