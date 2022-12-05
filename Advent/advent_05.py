from copy import deepcopy

PATH = "C:/Users/melvi/Desktop/Advent2022/Input/"

def parse_crates(file):
    crates = [[] for _ in range(9)]
    with open(file) as f:
        # iterate each line of the file
        for crate in f:
            # break when we've finished parsing the crates
            if len(crate) == 1:
                break
            # parse the corresponding crate to its crate stack
            crate_idx = 0
            for i in range(1, len(crate), 4):
                # if there is a crate, add it to the deque
                if crate[i] != ' ' and crate[i].isalpha():
                    crates[crate_idx].append(crate[i])

                # update the index pointer of the crate stack we are appending to
                crate_idx += 1
                if crate_idx % 9 == 0:
                    crate_idx = 0

    return [list(reversed(crate)) for crate in crates]

def parse_moves(file):
    moves = [] # where each move is a list of [# of crates, crate from #, crate to #]
    with open(file) as f:
        for move in f:
            # if the current line is one that is indicating a move
            if move[0] == 'm':
                _, num_crates, _, crate_from, _, crate_to = move.replace('\n', '').split(' ')
                moves.append([int(num_crates), int(crate_from), int(crate_to)])
    return moves

crates = parse_crates(PATH + 'input05.txt')
moves = parse_moves(PATH + 'input05.txt')

# part one
def sim_cratemover_9000(crate_stack, moves):
    crates = deepcopy(crate_stack)
    for move in moves:
        num_crates, crate_from, crate_to = move
        for _ in range(num_crates):
            popped_crate = crates[crate_from-1].pop()
            crates[crate_to-1].append(popped_crate)

    # return a list containing the top of crate at each crate stack
    return [crate[-1] for crate in crates]

print(f"The crates at the top of the stack after rearranging with the CrateMover9000 are: {''.join(sim_cratemover_9000(crates, moves))}")
# Output: The crates at the top of the stack after rearranging are: FJSRQCFTN

# part two
def sim_cratemover_9001(crate_stack, moves):
    crates = deepcopy(crate_stack)
    for move in moves:
        num_crates, crate_from, crate_to = move
        crates[crate_to-1].extend(crates[crate_from-1][-num_crates:])
        crates[crate_from-1] = crates[crate_from-1][:-num_crates]

    # return a list containing the top of crate at each crate stack
    return [crate[-1] for crate in crates]

print(f"The crates at the top of the stack after rearranging with the CrateMover9001 are: {''.join(sim_cratemover_9001(crates, moves))}")
# Output: The crates at the top of the stack after rearranging with the CrateMover9001 are: CJVLJQPHS