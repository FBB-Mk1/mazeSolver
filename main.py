from tkinter import Tk, BOTH, Canvas

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
    line1 = Line(Point(3,4), Point(30,40))
    line2 = Line(Point(333,400), Point(666,400))
    window.draw_line(line1, 'red')
    window.draw_line(line2, 'blue')
    window.wait_for_close()

main()