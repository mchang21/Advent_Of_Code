import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [list(l) for l in f.read().strip().split('\n')]
    return data

def transpose(matrix):
    return [list(r) for r in zip(*matrix)]

# rotates matrix by 90 degrees
def rotate(matrix):
    # transpose matrix
    matrix = transpose(matrix)
    m, n = len(matrix), len(matrix[0])
    # flip matrix
    for i in range(m):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    return matrix

def tilt(matrix):
    m,n = len(matrix), len(matrix[0])
    for i in range(m):
        swap = n-1
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '#':
                swap = j-1
            elif matrix[i][j] == 'O':
                # swap cells
                matrix[i][j], matrix[i][swap] = matrix[i][swap], matrix[i][j]
                swap -= 1
    return matrix

def calculate_load(matrix, rotates=0):
    # rotate back to original orientation
    for _ in range(rotates):
        matrix = rotate(matrix)
    # calculate load
    load, m = 0, len(matrix)
    for i, row in enumerate(matrix):
        count = row.count('O')
        load += (count * (m-i))
    return load

data = parse_data(file)

# part one
print(f"The total load on the north support beams is {calculate_load(tilt(rotate(data)), 3)}.")
# The total load on the north support beams is 106186.

# part two
def get_cycle_start(matrix, cycles, memo):
    for i in range(1, cycles+1):
        # simulate one spin cycle
        for _ in range(4):
            # tilts north -> west -> south -> east
            matrix = tilt(rotate(matrix))
        # snapshot of current state of the matrix
        state = tuple(map(tuple, matrix))
        # reached a cycle
        if state in memo:
            index_to_state = {index:state for state,index in memo.items()}
            # return: index:state, index of start of cycle, length of cycle
            return index_to_state, memo[state], i-memo[state]
        # new state
        else:
            memo[state] = i

def simulate_spin(matrix, cycles):
    index_to_state, start, cycle_length = get_cycle_start(matrix, cycles, {})
    index = start + ((cycles - start) % cycle_length)
    return calculate_load(index_to_state[index])

cycles = 1_000_000_000
print(f"The total load on the north support beams after {cycles} cycles is {simulate_spin(data, cycles)}.")
# The total load on the north support beams after 1000000000 cycles is 106390.
