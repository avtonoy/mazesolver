import time
from drawing import Point, Window
from geometry import Cell


class Maze():
    def __init__(self,
                 left_top_corner: Point,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 win: Window):
        self._left_top_corner = left_top_corner
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

    def _create_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        pos_x = self._left_top_corner.x + i * self._cell_size_x
        pos_y = self._left_top_corner.y + j * self._cell_size_y
        left_top_corner = Point(pos_x, pos_y)
        right_bottom_corner = Point(
            pos_x+self._cell_size_x, pos_y + self._cell_size_y)
        Cell(left_top_corner, right_bottom_corner, self._win).draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
