from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window


    def get_center(self):
        x = (self._x2 + self._x1) // 2
        y = (self._y2 + self._y1) // 2
        return Point(x, y) 

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)),'black')
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)),'white')
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)),'black')
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)),'white')
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)),'black')
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)),'white')
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)),'black')
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)),'white')
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        line = Line(self.get_center(), to_cell.get_center())

        if not undo:
            self._win.draw_line(line, 'gray')
        else:
            self._win.draw_line(line, 'red')