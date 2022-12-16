from queue import LifoQueue
from typing import Type, List

#current_dir: Type['Directory'] = None

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()

    current_dir: Type['Directory'] = None
    all_dirs: List['Directory'] = list()
    for l in lines:
        current_dir = process_line(l, current_dir, all_dirs)
        
    root = current_dir.get_parent()
    print("Name: " + root.name + " Dirs: " + str(len(root.dirs)) + " files: " + str(len(root.files)))
    print("Total size: " + str(root.get_total_size()))
    
    under_100k = 0
    for dir in all_dirs:
        this_dir = dir.get_total_size()
        if this_dir <= 100000:
            under_100k += this_dir
    print("Size under 100000: " + str(under_100k))
    
    # Total drive size = 70,000,000
    # Current used space = 48,044,502
    # Necessary free = 30,000,000
    # Must free 21955498
    # Find smallest directory that is at least 21955498
    
    to_delete = 0
    for dir in all_dirs:
        this_dir = dir.get_total_size()
        if this_dir >= 8044502 and (this_dir < to_delete or to_delete == 0):
            to_delete = this_dir
            
    print("delete: " + str(to_delete))

    
def process_line(line: str, dir: Type['Directory'], all_dirs: List['Directory']) -> Type['Directory']:
    line_bits = line.split(" ") 
 
    if line_bits[0] == "$":
        cmd = line_bits[1]
        if cmd == "cd":
            dir_name = line_bits[2].strip()
            # step out of a directory
            if dir_name == "..":
                return dir.parent
            else: # create a new directory and step into it
                if dir is None:
                    dir = Directory(dir_name, None)
                    all_dirs.append(dir)
                    return dir
                else:
                    dir = dir.add_dir(dir_name)
                    all_dirs.append(dir)
        # end if cd
    else:
        if line_bits[0] == "dir":
            pass # we'll get dirs later when cd'd
        else:
            dir.add_file(int(line_bits[0]))
            
    return dir
               

class File:
    '''File in a filesystem'''
    
    def __init__(self, size: int) -> None:
        self.size = size
        
    def __str__(self): 
        return str(self.size)
    
    def __repr__(self):
        return self.__str__()
    
class Directory:
    '''Directory in a filesystem'''
    
    def __init__(self, name: str, parent_dir = Type['Directory']) -> None:
        self.name = name
        self.parent = parent_dir
        self.dirs: List['Directory'] = list()
        self.files: List[File] = list()
        
    def add_dir(self, name: str) -> Type['Directory']:
        dir = Directory(name, self)
        self.dirs.append(dir)
        return dir
        
    def add_file(self, size: int) -> None:
        self.files.append(File(size))
        
    def get_total_size(self) -> int:
        # sum all files and all dirs
        dir_size = 0
        
        for d in self.dirs:
            dir_size += d.get_total_size()
            
        return dir_size + self.get_file_size()
    
    def get_file_size(self) -> int:
        file_size = 0
        
        for f in self.files:
            file_size += f.size
        return file_size
    
    def get_size_100k(self) -> int:
        # get the sum of all directories inside that are less than 100000
        # 
        accumulated_size = 0
        
        for d in self.dirs:
            check_dir = d.get_size_100k()
            if check_dir <= 100000:
                accumulated_size += check_dir
                
        # only count this dir if get_total_size is < 100k
        this = self.get_total_size()
        if this <= 100000:
            accumulated_size += this
            
        return accumulated_size
        
    def get_parent(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_parent()
        
    def __str__(self): 
        return self.name
    
    def __repr__(self):
        return self.__str__()
        
    