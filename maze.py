from cell import Cell
import time
import random


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        
      
    def _create_cells(self):
        for i in range(self.num_cols):
            cols = []
            for j in range(self.num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
        

    def _draw_cell(self, i, j, debug=False):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2, debug)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        #time.sleep(0.05)
        
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            #cells to visit
            #left
            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append((i-1, j))
            #right
            if i < self.num_cols - 1 and not self._cells[i + 1][j]._visited:
                to_visit.append((i+1, j))
            #top
            if j > 0 and not self._cells[i][j - 1]._visited: 
                to_visit.append((i, j-1))
            #bottom
            if j < self.num_rows - 1 and not self._cells[i][j + 1]._visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            rand = random.randrange(len(to_visit))
            next = to_visit[rand]
            if next[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next[0] == i - 1 :
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next[1] == j + 1 :
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            self._break_walls_r(next[0], next[1])