from drawing import Point, Window, Line
import time


class Cell():
    def __init__(self,
                 left_top_corner: Point,
                 right_bottom_corner: Point,
                 win: Window,
                 has_left_wall: bool = True,
                 has_right_wall: bool = True,
                 has_top_wall: bool = True,
                 has_bottom_wall: bool = True
                 ):
        self._left_top_corner = left_top_corner
        self._right_bottom_corner = right_bottom_corner
        self._left_bottom_corner = Point(
            left_top_corner.x, right_bottom_corner.y)
        self._right_top_corner = Point(
            right_bottom_corner.x, left_top_corner.y)
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        mid_x = (right_bottom_corner.x - left_top_corner.x) / \
            2 + left_top_corner.x
        mid_y = (left_top_corner.y - right_bottom_corner.y) / \
            2 + right_bottom_corner.y
        self._mid = Point(mid_x, mid_y)

    def draw(self) -> None:
        if self.has_left_wall:
            self._win.draw_line(
                Line(self._left_top_corner, self._left_bottom_corner))
        if self.has_right_wall:
            self._win.draw_line(
                Line(self._right_top_corner, self._right_bottom_corner))
        if self.has_top_wall:
            self._win.draw_line(
                Line(self._left_top_corner, self._right_top_corner))
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(self._left_bottom_corner, self._right_bottom_corner))

    def draw_move(self, to_cell, undo: bool = False):
        if undo:
            color = 'gray'
        else:
            color = 'red'
        l = Line(self._mid, to_cell._mid)
        self._win.draw_line(l, color)


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
