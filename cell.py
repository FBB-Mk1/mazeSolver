from graphics import Line, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
        self.__top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self.__left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self.__right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self.__bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        
    def get_center(self):
        x = (self._x2 + self._x1) // 2
        y = (self._y2 + self._y1) // 2
        print(x, y)
        return Point(x, y) 

    def draw(self):
        if self.has_top_wall:
            self._win.draw_line(self.__top,'black')
        if self.has_left_wall:
            self._win.draw_line(self.__left,'black')
        if self.has_right_wall:
            self._win.draw_line(self.__right,'black')
        if self.has_bottom_wall:
            self._win.draw_line(self.__bottom,'black')
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center(), to_cell.get_center())

        if not undo:
            self._win.draw_line(line, 'gray')
        else:
            self._win.draw_line(line, 'red')