from queue import LifoQueue
from typing import Type, List

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()
    rows = load_forest(lines)
        
    # part 1
    visible_trees = get_visible_tree_count(rows)
    print(f'visible trees: {visible_trees}')
    
    # part 2
    print(f'best scenic score: {find_best_scenic(rows)}')
    
def find_best_scenic(trees) -> int:
    best_scenic = 0
    for row_index, tree_row in enumerate(trees):
        for tree_index, tree in enumerate(tree_row):
            scenic_score = get_scenic_score(row_index, tree_index, trees)
            if scenic_score > best_scenic:
                best_scenic = scenic_score
            
    return best_scenic
        # calculate the viewing distance in each direction
        # to do so, find how far away is the closest tree that is same or taller
        # multiple viewing distances by each other
    
def get_scenic_score(row_index: int, tree_index: int, trees: list[list[str]]) -> int:
    """calculates the scenic score for a given tree. This is determined based on how many trees can be 
    seen from a given spot

    Args:
        row_index (int): index of row for given tree to check
        tree_index (int): index of column for given tree to check
        trees (list[list[str]]): all trees

    Returns:
        int: scenic score
    """
    if is_border_tree(row_index, tree_index, trees):
        # border trees have at least one directional value of 0, thus they'll always be zero scenic score 
        return 0
    
    tree_row = trees[row_index]      
    tree_height = int(tree_row[tree_index])
    # check left of tree
    num_trees_visible_left = get_visible_horiz(tree_row, tree_height, tree_range=range(tree_index - 1, -1, -1))
    num_trees_visible_right = get_visible_horiz(tree_row, tree_height, tree_range=range(tree_index + 1, len(tree_row)))
    num_trees_visible_up = get_visible_vert(tree_index, range(row_index - 1, -1, -1), tree_height, trees)
    num_trees_visible_down = get_visible_vert(tree_index, range(row_index + 1, len(trees)), tree_height, trees)

    scenic = num_trees_visible_left * num_trees_visible_right * num_trees_visible_up * num_trees_visible_down
    return scenic

def get_visible_horiz(row: list[str], tree_height: int, tree_range) -> int:
    count = 0
    for i in tree_range:
        count += 1
        if int(row[i]) >= tree_height:
            # stop counting because the view is blocked
            break
    return count
    
def get_visible_vert(tree_index: int, tree_range, tree_height: int, trees:list[list[str]]) -> bool:
    count = 0
    for row_to_check in tree_range:
        count += 1
        if int(trees[row_to_check][tree_index]) >= tree_height:
            # stop counting because the view is blocked
            break
    return count
    
def load_forest(lines: list[str]) -> list[list[str]]:
    forest = []
    for line in lines:
        row = list(line.strip())
        forest.append(row)
    return forest

def get_visible_tree_count(trees: list[list[str]]) -> int:

    count = 0
    for row_index, tree_row in enumerate(trees):
        for tree_index, tree in enumerate(tree_row):

            if is_tree_visible(row_index, tree_index, trees):
                count +=1
    return count

def is_tree_visible(row_index: int, tree_index: int, trees: list[list[str]]) -> bool:
    if is_border_tree(row_index, tree_index, trees):
                return True
    
    tree_row = trees[row_index]      
    tree_height = int(tree_row[tree_index])
    # check left of tree
    if is_visible_horiz(tree_row, tree_height, tree_range=range(tree_index - 1, -1, -1)):
        return True
    # check right of tree
    elif is_visible_horiz(tree_row, tree_height, tree_range=range(tree_index + 1, len(tree_row))):
        return True
    # check up
    elif is_visible_vert(tree_index, range(row_index - 1, -1, -1), tree_height, trees):
        return True
    # check down
    elif is_visible_vert(tree_index, range(row_index + 1, len(trees)), tree_height, trees):
        return True
    else:
        return False

def is_border_tree(row_index: int, col_index: int, trees:list[list[str]]) -> bool:
    # is a border tree if in first/last row, or first/last column
    if row_index == 0 or col_index == 0:
        return True
    elif row_index == len(trees):
        return True
    elif col_index == len(trees[row_index]):
        return True
    else:
        return False

def is_visible_horiz(row: list[str], tree_height: int, tree_range) -> bool:
    for i in tree_range:
        if int(row[i]) >= tree_height:
            return False
        
    # if no tree was at least as tall as tree_height, then it's visible
    return True
  
def is_visible_vert(tree_index: int, tree_range, tree_height: int, trees:list[list[str]]) -> bool:
    for row_to_check in tree_range:
        if int(trees[row_to_check][tree_index]) >= tree_height:
            return False

    # if no tree was at least as tall as tree_height, then it's visible
    return True
  