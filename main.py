from graphics import Window
from line import Line
from point import Point
from cell import Cell

win = Window(800, 600)
p1 = Point(25, 25) 
p2 = Point(50, 50)
cell = Cell(p1, p2, win)
cell.draw()
win.wait_for_close()