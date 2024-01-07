from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tk = Tk()
        self.tk.title('Maze Solver')
        self.tk.geometry(f'{self.width}x{self.height}')
        self.canvas = Canvas(self.tk, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.tk.protocol('WM_DELETE_WINDOW', self.close)
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.tk.update_idletasks()
        self.tk.update()

    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False


        