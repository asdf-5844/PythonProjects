from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # Create an oval
        self.canvas.move(self.id, 245, 100) # Move the oval to the middle of the canvas
        starts  = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0] # Start random from range -3 to 3
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() # Canvas height
        self.canvas_width = self.canvas.winfo_width() # Canvas width
        self.hit_bottom = False # Not on bottom

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) # Position of the paddle
        # If the right side of the ball is greater than the left side of the paddle...
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            # If the bottom of the ball is between the paddle's top and bottom...
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) # Move ball by self.x & self.y
        pos = self.canvas.coords(self.id) # Current X and Y coordinates
        if pos[1] <= 0: # If the top of the ball hits the top of the screen
            self.y = 3
        if pos[3] >= self.canvas_height: # If the bottom of the ball hits the bottom of the canvas
            self.hit_bottom = True # Game will END
        # If hit_paddle function returns true, we change the direction of the ball
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0: # If the left of the ball hits the left side of the screen
            self.x = 3
        if pos[2] >= self.canvas_width: # If the right of the ball hits the right side of the screen
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # Create a rectangle for the paddle
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width() # Get canvas width
        # Make the paddle respond to left/right arrow keys
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0) # Move paddle
        pos = self.canvas.coords(self.id) # Position of the paddle
        if pos[0] <= 0: # If the left of the paddle hits the left side of the screen
            self.x = 0 # Stop moving
        elif pos[2] >= self.canvas_width: # If the right of the paddle hits the right side of the screen
            self.x = 0
    
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

tk = Tk()
tk.title("Game") # Window title
tk.resizable(0, 0) # Not resizable
tk.wm_attributes("-topmost", 1) # Place our window in front of other windows
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) # Set canvas
canvas.pack() # Initialize the canvas
tk.update() # Initialize tkinter

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

# Main loop that constantly tells tkinter to do it

game_started = False

def start_game(event):
    global game_started
    game_started = True

canvas.bind("<Button-1>", start_game)

while 1:
    if game_started and not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    elif ball.hit_bottom:
        canvas.create_text(200, 250, text="Game Over!", font=("Times", 30), fill="black")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
