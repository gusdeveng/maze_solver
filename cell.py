from point import Point
from tkinter import Tk, BOTH, Canvas
from line import Line

class Cell:
    def __init__(self, p1, p2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self._win = win;

    def draw(self):
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))

    def draw_move(self, to_cell, undo=False):
        color = 'red'
        if undo: 
            color = 'gray'
        #left to right
        if self._x1 < to_cell._x2 and self._y2 == to_cell._y2:
            mid_x1 = (self._x1 + self._x2) / 2
            mid_x2 = (to_cell._x1 + to_cell._x2) / 2
            mid_y = (self._y1 + to_cell._y2) / 2
            self._win.draw_line(Line(Point(mid_x1, mid_y), Point(mid_x2, mid_y)), color)
        #right to left
        if self._x2 > to_cell._x1 and self._y2 == to_cell._y2:
            mid_x1 = (self._x1 + self._x2) / 2
            mid_x2 = (to_cell._x1 + to_cell._x2) / 2
            mid_y = (self._y1 + to_cell._y2) / 2
            self._win.draw_line(Line(Point(mid_x1, mid_y), Point(mid_x2, mid_y)), color)
        #top to bottom
        if self._x2 == to_cell._x2 and self._y1 < to_cell._y2:
            mid_y1 = (self._y1 + self._y2) / 2
            mid_y2 = (to_cell._y1 + to_cell._y2) / 2
            mid_x = (self._x1 + to_cell._x2) / 2
            self._win.draw_line(Line(Point(mid_x, mid_y1), Point(mid_x, mid_y2)), color)
        #bottom to top 
        if self._x2 == to_cell._x2 and to_cell._y1 < self._y2:
            mid_y1 = (self._y1 + self._y2) / 2
            mid_y2 = (to_cell._y1 + to_cell._y2) / 2
            mid_x = (self._x1 + to_cell._x2) / 2
            self._win.draw_line(Line(Point(mid_x, mid_y1), Point(mid_x, mid_y2)), color)
