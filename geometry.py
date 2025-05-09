from drawing import Point, Window, Line


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
