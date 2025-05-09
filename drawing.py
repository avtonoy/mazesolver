from tkinter import Tk, BOTH, Canvas

class Point(): 
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1: Point, p2: Point) -> None:
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y

    def draw(self, canvas: Canvas, fill_color: str = 'black') -> None:
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)



class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = 'MazeSolver 2000'
        self.__canvas = Canvas(
            master=self.__root, background='white', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = False

    def draw_line(self,line:Line,fill_color:str='black'):
        line.draw(self.__canvas,fill_color=fill_color)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


