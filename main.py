from tkinter import Tk, BOTH, Canvas

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

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2 
    
    def draw(self, canvas, fill_color):
        canvas.create_line( self.point1.x, self.point1.y,  self.point2.x, self.point2.y, fill = fill_color, width = 2)
        canvas.pack()

class Window:
    def __init__(self, width=400, height=400):
        self.__root = Tk()
        self.__root.title('Window')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(expand=True, fill=BOTH)

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

def main():
    window = Window(1024, 768)
    cell1 = Cell(10,10,30,30, window)
    cell1.draw()
    cell2 = Cell(30,10,50,30, window)
    cell2.draw()
    cell1.draw_move(cell2, True)
    window.wait_for_close()

main()