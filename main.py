from drawing import Line, Window, Point
from geometry import Cell


def main():
    print("Hello from mazesolver!")
    win = Window(800, 800)
    line = Line(Point(0, 0), Point(200, 200))
    win.draw_line(line)
    c = Cell(Point(100, 100), Point(300, 300), win)
    c.has_bottom_wall = False
    c.draw()
    c2 = Cell(Point(200,200),Point(400,400),win)
    c2.draw()
    c.draw_move(c2)
    c3 = Cell(Point(200,500),Point(400,700),win)
    c3.draw()
    c2.draw_move(c3,True)
    win.wait_for_close()


if __name__ == "__main__":
    main()
