from drawing import Point, Window, Line


class Cell():
    def __init__(self,
                 left_top_corner: Point,
                 right_bottom_corner: Point,
                 win: Window = None,
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

        self._has_wall_color = 'black'
        self._has_no_wall_color = 'white'

    def draw(self) -> None:

        if self.has_left_wall:
            color = self._has_wall_color
        else:
            color = self._has_no_wall_color
        self._win.draw_line(
            Line(self._left_top_corner, self._left_bottom_corner), color)

        if self.has_right_wall:
            color = self._has_wall_color
        else:
            color = self._has_no_wall_color
        self._win.draw_line(
            Line(self._right_top_corner, self._right_bottom_corner), color)

        if self.has_top_wall:
            color = self._has_wall_color
        else:
            color = self._has_no_wall_color
        self._win.draw_line(
            Line(self._left_top_corner, self._right_top_corner), color)

        if self.has_bottom_wall:
            color = self._has_wall_color
        else:
            color = self._has_no_wall_color
        self._win.draw_line(
            Line(self._left_bottom_corner, self._right_bottom_corner), color)

    def draw_move(self, to_cell, undo: bool = False):
        if undo:
            color = 'gray'
        else:
            color = 'red'
        l = Line(self._mid, to_cell._mid)
        self._win.draw_line(l, color)
