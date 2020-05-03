from tkinter import*
from random import*
import time
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
    def drow(self):
        self.canvas.move(self.id, 0, -1)
tk = Tk()
tk.title('game')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height=400, bd=0, highlightthickness = 0)
canvas.pack() 
tk.update()
ball = Ball(canvas,'red')
while 1:
    ball.drow()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
   
