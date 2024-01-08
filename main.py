from graphics import Window
from line import Line
from point import Point
from cell import Cell

win = Window(800, 600)
cell1 = Cell(Point(25,25), Point(50,50), win, has_bottom_wall=False, has_right_wall=False)
cell2 = Cell(Point(50,25), Point(75,50), win, has_left_wall=False, has_bottom_wall=False)
cell3 = Cell(Point(50,50), Point(75,75), win, has_left_wall=False, has_top_wall=False)
cell4 = Cell(Point(25,50), Point(50,75), win, has_right_wall=False, has_top_wall=False)
cell1.draw();
cell2.draw();
cell3.draw();
cell4.draw();
cell1.draw_move(cell2)
cell2.draw_move(cell3)
cell3.draw_move(cell4)
cell4.draw_move(cell1)
win.wait_for_close()