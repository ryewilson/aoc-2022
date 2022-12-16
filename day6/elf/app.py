from collections import deque

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readline()
    
    num_processed = process_chars_for_pattern(lines)
    
    print("num processed until marker: " + str(num_processed))

    
def process_chars_for_pattern(line="") -> int:
    # scan  through chars and look for 4 different chars
    tracked_chars = deque((" ", " ", " ", " "), 14)
    total_chars = 0
    
    for c in line:
        if len(tracked_chars) >= 14:
            tracked_chars.popleft()
        tracked_chars.append(c)
        total_chars += 1

        if last_four_are_different(tracked_chars):
            return total_chars
        
    print(str(tracked_chars))
        
def last_four_are_different(four_chars: deque):

    char_set = set(four_chars)
    print("set: " + str(char_set))
    # if the set has 4/14 items then they must be all unique
    if len(char_set) is 14:
        return True
    else:
        return False
       
    
class HelperClass:
    '''Add description here'''
    
    def __init__(self, strRange="") -> None:
        pass
        
    def __str__(self): 
        return "implement this"
    
    def __repr__(self):
        return self.__str__()
        