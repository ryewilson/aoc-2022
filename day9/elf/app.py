from queue import LifoQueue
from typing import Type, List
from enum import Enum

class Direction(Enum):
    U = 1
    D = 2
    L = 3
    R = 4

def run():
    """main entry point
    """
    # Load the file
    # input
    with open('input.txt') as f:
        lines = f.readlines()

    rope = run_simulation(lines)
    print (rope.get_tail_position_count())

    
def run_simulation(lines: list[str]) -> Type['RopePosition']:
    rope = RopePosition()
    for cmd in lines:
        dir_and_value = cmd.strip().split()
        rope.move(get_direction(dir_and_value[0]), int(dir_and_value[1]))
        
    return rope

def get_direction(dir_str: str) -> Type[Direction]:
    return Direction[dir_str]

class RopePoint:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    
class RopePosition:
    '''Simulates a rope with head and tail. Tail always follows head'''
    
    def __init__(self) -> None:
        self.tail_positions = []
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
    
    # Q's
    # how to track unique tail spots? -> 2d list? 1dlist with x,y coordinates as string, then "get unique elements"
    
    def move(self, direction: Type[Direction], value: int) -> None:
        # simulate array by tracking position of H and T? (x-y coordinates)
        # each call to this method moves the head in one direction
        for _ in range(0, value):
            print(self.__str__())
            match direction:
                case Direction.U:
                    self.move_up()
                case Direction.D:
                    self.move_down()
                case Direction.L:
                    self.move_left()
                case Direction.R:
                    self.move_right()
        
    def move_up(self):
        self.move_vert(1)
        
    def move_down(self):
        self.move_vert(-1)
    
    def move_vert(self, increment_by:int) -> None:
        self.head_y += increment_by
        # if tail is more than 1 space away, move closer
        if abs(self.tail_y - self.head_y) > 1:
            if self.tail_x != self.head_x:
                # if H and T aren't in the same column then 
                # need to move one x AND one y
                if self.head_x > self.tail_x:
                    self.tail_x += 1
                else:
                    self.tail_x -= 1
            self.tail_y += increment_by
        self.track_tail_position()
        
    def move_right(self):
        self.move_hor(1)
        
    def move_left(self):
        self.move_hor(-1)
        
    def move_hor(self, increment_by:int) -> None:
        self.head_x += increment_by
        # if tail is more than 1 space away, move closer
        if abs(self.tail_x - self.head_x) > 1:
            if self.tail_y != self.head_y:
                # if H and T aren't in the same row then 
                # need to move one x AND one y
                if self.head_y > self.tail_y:
                    self.tail_y += 1
                else:
                    self.tail_y -= 1
            self.tail_x += increment_by
        self.track_tail_position()
        
    def track_tail_position(self):
        combined_position = f'{self.tail_x},{self.tail_y}'
        if combined_position not in self.tail_positions:
            self.tail_positions.append(combined_position)
        
        
    def get_tail_position_count(self) -> int:
        return len(self.tail_positions)
        
    def __str__(self): 
        return  f'head: {self.head_x},{self.head_y} - tail: {self.tail_x},{self.tail_y}'
    
    def __repr__(self):
        return self.__str__()
        
        
