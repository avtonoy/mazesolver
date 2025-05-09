from drawing import *


def main():
    print("Hello from mazesolver!")
    win = Window(400,400)
    line = Line((0,0),(200,200))
    win.draw_line(line)
    win.wait_for_close()
    



        
if __name__ == "__main__":
    main()
