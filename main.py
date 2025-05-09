from drawing import Line, Window, Point
from geometry import Cell


def main():
    print("Hello from mazesolver!")
    win = Window(400, 400)
    line = Line(Point(0, 0), Point(200, 200))
    win.draw_line(line)
    c = Cell(Point(100, 100), Point(300, 300), win)
    c.has_bottom_wall = False
    c.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
