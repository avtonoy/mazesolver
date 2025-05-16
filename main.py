from drawing import Line, Window, Point
from geometry import Cell
from maze import Maze


def main():
    print("Hello from mazesolver!")
    win = Window(800, 800)
    maze = Maze(Point(100, 100), 10, 10, 50, 50, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
