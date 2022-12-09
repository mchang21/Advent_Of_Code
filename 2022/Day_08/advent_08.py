PATH = '../Advent_Of_Code/2022/Day_08/'

def parse_tree_heights(file):
    tree_heights = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            current_row = []
            for height in line:
                current_row.append(int(height))
            tree_heights.append(current_row)
    return tree_heights

# part one
def check_visibility(trees, tree_height, row, col):
    north, south, east, west = True, True, True, True

    # checks if there are any trees blocking visibility
    # check north
    for r in range(row-1, -1, -1):
        if trees[r][col] >= tree_height:
            north = False
            break
    # check south
    for r in range(row+1, len(trees)):
        if trees[r][col] >= tree_height:
            south = False
            break
    # check east
    for c in range(col+1, len(trees[0])):
        if trees[row][c] >= tree_height:
            east = False
            break
    # check west
    for c in range(col-1, -1, -1):
        if trees[row][c] >= tree_height:
            west = False
            break
    # returns true if the tree is visible from a direction
    return any([north, south, east, west])

def count_visible_trees(trees):
    trees_visible = (len(trees) * 2) + ((len(trees)-2) * 2) # initial number of trees on the edge

    # for each tree within the edges
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees[0])-1):
            if check_visibility(trees, trees[i][j], i, j):
                trees_visible += 1
    return trees_visible

# part two
def calculate_scenic_score(trees, tree_height, row, col):
    north, south, east, west = 0, 0, 0, 0
    # check north
    for r in range(row-1, -1, -1):
        if trees[r][col] <= tree_height:
            north += 1
            if trees[r][col] == tree_height:
                break
    # check south
    for r in range(row+1, len(trees)):
        if trees[r][col] <= tree_height:
            south += 1
            if trees[r][col] == tree_height:
                break
    # check east
    for c in range(col+1, len(trees[0])):
        if trees[row][c] <= tree_height:
            east += 1
            if trees[row][c] == tree_height:
                break
    # check west
    for c in range(col-1, -1, -1):
        if trees[row][c] <= tree_height:
            west += 1
            if trees[row][c] == tree_height:
                break
    return north * south * east * west

def find_highest_scenic_score(trees):
    highest_scenic_score = 0
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees[0])-1):
            highest_scenic_score = max(highest_scenic_score, calculate_scenic_score(trees, trees[i][j], i, j))
    
    return highest_scenic_score

trees = parse_tree_heights(PATH + 'input.txt')
print(f"The number of visible trees are {count_visible_trees(trees)}") # part one 
# Output: The number of visible trees are 1843
print(f"The highest scenic score is {find_highest_scenic_score(trees)}") # part two
# Output: The highest scenic score is 180000