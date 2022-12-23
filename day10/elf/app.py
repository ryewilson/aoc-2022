from queue import LifoQueue
from typing import Type, List

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()

    # do something to each line and create a list with the resulting items
    #splitLines = [process_line(x) for x in lines] 

    

    
class HelperClass:
    '''Add description here'''
    
    def __init__(self, strRange="") -> None:
        pass
        
    def __str__(self): 
        return "implement this"
    
    def __repr__(self):
        return self.__str__()
        