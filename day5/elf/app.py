
from queue import LifoQueue
from typing import Type

class Warehouse:
    '''Stores crates'''
    
    def initialize_stack(*items):
        stack = LifoQueue(maxsize=60)
        for value in items:
            stack.put(value)
        return stack
    
    col_1 = initialize_stack("R", "S", "L", "F", "Q")
    col_2 = initialize_stack("N", "Z", "Q", "G", "P", "T")
    col_3 = initialize_stack("S", "M", "Q", "B")
    col_4 = initialize_stack("T", "G", "Z", "J", "H", "C", "B", "Q")
    col_5 = initialize_stack("P", "H", "M", "B", "N", "F", "S")
    col_6 = initialize_stack("P", "C", "Q", "N", "S", "L", "V", "G")
    col_7 = initialize_stack("W", "C", "F")
    col_8 = initialize_stack("Q", "H", "G", "Z", "W", "V", "P", "M")
    col_9 = initialize_stack("G", "Z", "D", "L", "C", "N", "R")
    
    all_stacks = {1: col_1, 2: col_2, 3: col_3, 4: col_4, 5: col_5, 6:col_6, 7:col_7, 8:col_8, 9:col_9}
    
    def get_stack(self, num: int) -> LifoQueue:
        return self.all_stacks[num]
        
    def print_top(self) -> None:
        print(self.col_1.get(), self.col_2.get(), self.col_3.get(),self.col_4.get(), self.col_5.get(), self.col_6.get(), self.col_7.get(), self.col_8.get(), self.col_9.get())
        
    def __str__(self): 
        return self.col_1.__str__()
    
    def __repr__(self):
        return self.__str__()

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()

    # line 11 starts the commands
    commands = lines[10: ]
    # handle "move x from stack-y to stack-z" command
    wh = Warehouse()
    
    for l in commands:
        process_command(l, wh)
        
    # need top letter of each stack
    wh.print_top()

    
def process_command(line: str, wh: Type[Warehouse]):
    # split on " "
    line_commands = line.strip().split(" ") 
    # ignore 0, 2, 4
    # 1 = how many crates to move
    # 3 = source stack
    # 5 = dest stack
    print(line_commands)
    num_crates = int(line_commands[1])
    source = int(line_commands[3])
    dest = int(line_commands[5])
    
    move_crates(wh, num_crates, source, dest)
    
def move_crates(wh: Type[Warehouse], num: int, source: int, dest: int):
    source_stack = wh.get_stack(source)
    dest_stack = wh.get_stack(dest)
    
    temp_stack = LifoQueue(50)

    for val in range(num):
        crate = source_stack.get() 
        temp_stack.put(crate)
        
    for crate in range(num):
        dest_stack.put(temp_stack.get())


    
    
        