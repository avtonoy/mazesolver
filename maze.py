import time
from drawing import Point, Window
from geometry import Cell
import random



class Maze():
    def __init__(self,
                 left_top_corner: Point,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 win: Window = None, 
                 seed_for_random:int = None):
        self._left_top_corner = left_top_corner
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        
        
        self._max_i = num_cols - 1
        self._min_i = 0 
        self._max_j = num_rows - 1
        self._min_j = 0 
        
        if seed_for_random != None: random.seed(seed_for_random)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _create_cells(self):

        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                pos_x = self._left_top_corner.x + i * self._cell_size_x
                pos_y = self._left_top_corner.y + j * self._cell_size_y
                left_top_corner = Point(pos_x, pos_y)
                right_bottom_corner = Point(
                    pos_x+self._cell_size_x, pos_y + self._cell_size_y)

                self._cells[i].append(
                    Cell(left_top_corner, right_bottom_corner, self._win))
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        # break entrance
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(-1, -1)
        
    def _reset_cells_visited(self):
        ln_i=self._num_cols
        ln_j=self._num_rows
        for i in range(ln_i): 
            for j in range(ln_j): 
                self._cells[i][j].visited = False
    
    def _get_neighbours_visitable(self,i,j) -> list[tuple[int,int,str]]:
        visitable = []
        # left
        x = i - 1
        if x >= self._min_i: 
            if self._cells[x][j].visited == False: 
                visitable.append((x,j,'left'))                
        # top
        x = j - 1
        if x >= self._min_j: 
            if self._cells[i][x].visited == False:
                visitable.append((i,x,'top'))         
        # right
        x = i + 1
        if x <= self._max_i: 
            if self._cells[x][j].visited == False: 
                visitable.append((x,j,'right'))                
        # bottom
        x = j + 1
        if x <= self._max_j:
            if self._cells[i][x].visited == False: 
                visitable.append((i,x,'bottom'))
        return visitable
    
    def _knock_down_wall(self, current_cell:Cell,choosen_cell:Cell,direction:str): 
        match direction: 
            case 'top': 
                current_cell.has_top_wall = False
                choosen_cell.has_bottom_wall = False
            case 'bottom': 
                current_cell.has_bottom_wall = False
                choosen_cell.has_top_wall = False 
            case 'left': 
                current_cell.has_left_wall = False
                choosen_cell.has_right_wall = False
            case 'right': 
                current_cell.has_right_wall = False
                choosen_cell.has_left_wall = False
    
    def _break_walls_r(self,i,j): 
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True: 
            list_to_visit = self._get_neighbours_visitable(i,j)
            lng_visitable = len(list_to_visit)
            if len(list_to_visit) == 0: 
                current_cell.draw()
                return
            picked_to_visit:tuple = list_to_visit[random.randint(0,lng_visitable-1)]
            picked_cell = self._cells[picked_to_visit[0]][picked_to_visit[1]]
            picked_direction = picked_to_visit[2]
            self._knock_down_wall(current_cell,picked_cell,picked_direction)
            current_cell.draw()
            self._break_walls_r(picked_to_visit[0],picked_to_visit[1])
    

    def _draw_cell(self, i, j):
        if self._win != None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        # time.sleep(0.05)
