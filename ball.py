from tkinter import*
import random
import time
class Stick:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right) 
    def drow(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id) 
                                                                             
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        pos = self.canvas.coords(self.id) 
        if pos[0] > 0: 
            self.x = -2
    def turn_right(self, evt):
        pos = self.canvas.coords(self.id) 
        if pos[2] < self.canvas_width: 
            self.x = 2

class Score: 
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text = self.score, fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text = self.score)     
                     
class Ball:
    def __init__(self, canvas, stick, score, color):
        self.canvas = canvas
        self.stick = stick
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        randomer = [-3, -2, -1, 1, 2, 3]
        random.shuffle(randomer)
        self.x = randomer[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_stick(self, pos):
        stick_pos = self.canvas.coords(self.stick.id)
        if pos[2] >= stick_pos[0] and pos[0] <= stick_pos[2]:
            if pos[3] >= stick_pos[1] and pos[3] <= stick_pos[3]:
                self.score.hit() 
                return True
        return False    
    def drow(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -1
        if self.hit_stick(pos) == True: ##
            self.y = -1
            
tk = Tk()
tk.title('game')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height=400, bd=0, highlightthickness = 0)
canvas.pack() 
tk.update()
stick = Stick(canvas, 'black')
score = Score(canvas, 'green')
ball = Ball(canvas, stick, score, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.drow()
        stick.drow()
    if ball.hit_bottom == True:
        time.sleep(0.5)
        game_over_text = canvas.create_text(250,200, font=("Purisa", 25), text= 'The end of the game: '+ str(score.score), state = 'normal')
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.004)
