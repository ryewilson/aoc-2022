
def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()

    splitLines = [process_line(x) for x in lines] 
    # Part 1 answer
    result = [True if is_fully_contained(sl[0], sl[1]) else False for sl in splitLines]
    num_full_overlap = result.count(True)
    print("Fully contained overlaps: " + str(num_full_overlap))
    
    # Part 2 answer
    result = [True if is_partially_contained(sl[0], sl[1]) else False for sl in splitLines]
    num_partial_overlap = result.count(True)
    print("Partially contained overlaps: " + str(num_partial_overlap))
    
def process_line(line=""):
    # split on ,
    bothElves = line.split(",") 
    return ElfSector(bothElves[0]), ElfSector(bothElves[1])

def is_fully_contained(elf1, elf2):
    if elf1.sectors.issubset(elf2.sectors):
        return True
    elif elf2.sectors.issubset(elf1.sectors):
        return True
    else:
        return False
    
def is_partially_contained(elf1, elf2):
    if elf1.sectors.isdisjoint(elf2.sectors):
        return False
    else:
        return True
    
class ElfSector:
    '''Represents  an elves cleaning assignments for some number of sectors'''
    
    sectors = set()
    
    def __init__(self, strRange="") -> None:
        sector_ends = strRange.split("-")
        self.sectors = set(range(int(sector_ends[0]), int(sector_ends[1])+ 1))
        
    def __str__(self): 
        return self.sectors.__str__()
    def __repr__(self):
        return self.__str__()
        