from graphics import Window
from cell import Cell


def main():
    window = Window(1024, 768)
    cell1 = Cell(10,10,30,30, window)
    cell1.draw()
    cell2 = Cell(30,10,50,30, window)
    cell2.draw()
    cell1.draw_move(cell2, True)
    window.wait_for_close()

main()