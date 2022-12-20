from queue import LifoQueue
from typing import Type, List
from enum import Enum

class Direction(Enum):
    U = 1
    D = 2
    L = 3
    R = 4
    
class RopeMarker(Enum):
    HEAD = 1
    TAIL = 2
    MIDDLE = 3

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
    
    def __init__(self, marker=RopeMarker.MIDDLE) -> None:
        self.x = 0
        self.y = 0
        self.marker = marker

    
class RopePosition:
    '''Simulates a rope with head and tail. Tail always follows head'''
    
    def __init__(self) -> None:
        self.tail_positions = []
        #self.all_knots = [RopePoint(RopeMarker.HEAD), RopePoint(RopeMarker.TAIL)]
        self.all_knots = [RopePoint(RopeMarker.HEAD), RopePoint(), RopePoint(), RopePoint(), RopePoint(), RopePoint(), RopePoint(), RopePoint(), RopePoint(), RopePoint(RopeMarker.TAIL)]
        
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
        next_moved = True
        
        # head always moves
        self.all_knots[0].y += increment_by
        
        for index,current_knot in enumerate(self.all_knots):
            if current_knot.marker != RopeMarker.TAIL and next_moved:
                next_moved = False
                next_knot = self.all_knots[index + 1]
                # if tail is more than 1 space away, move closer
                if abs(next_knot.y - current_knot.y) > 1:
                    if next_knot.x != current_knot.x:
                        # if H and T aren't in the same column then 
                        # need to move one x AND one y
                        if current_knot.x > next_knot.x:
                            next_knot.x += 1
                        else:
                            next_knot.x -= 1
                    next_knot.y += increment_by
                    next_moved = True # only continue moving knots if this one moved
                    
                if next_knot.marker == RopeMarker.TAIL:
                    self.track_tail_position()
        
    def move_right(self):
        self.move_hor(1)
        
    def move_left(self):
        self.move_hor(-1)
        
    def move_hor(self, increment_by:int) -> None:
        next_moved = True
        self.all_knots[0].x += increment_by

        for index,current_knot in enumerate(self.all_knots):
            # Only continue if we're not at the tail
            if current_knot.marker != RopeMarker.TAIL and next_moved:
                next_moved = False
                next_knot = self.all_knots[index + 1]
                
                # if tail is more than 1 space away, move closer
                if abs(next_knot.x - current_knot.x) > 1:
                    if next_knot.y != current_knot.y:
                        # if H and T aren't in the same row then 
                        # need to move one x AND one y
                        if current_knot.y > next_knot.y:
                            next_knot.y += 1
                        else:
                            next_knot.y -= 1
                    next_knot.x += increment_by
                    next_moved = True
                    
                if next_knot.marker == RopeMarker.TAIL:
                    self.track_tail_position()
        
    def track_tail_position(self):
        num_knots = len(self.all_knots)
        combined_position = f'{self.all_knots[num_knots - 1].x},{self.all_knots[num_knots - 1].y}'
        if combined_position not in self.tail_positions:
            self.tail_positions.append(combined_position)
        
        
    def get_tail_position_count(self) -> int:
        return len(self.tail_positions)
        
    def __str__(self): 
        num = len(self.all_knots)
        return  f'head: {self.all_knots[0].x},{self.all_knots[0].y} - tail: {self.all_knots[num-1].x},{self.all_knots[num-1].y}'
    
    def __repr__(self):
        return self.__str__()
        
        
