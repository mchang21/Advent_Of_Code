import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [l.split() for l in f.read().strip().split('\n')]
        for i, line in enumerate(data):
            sizes = tuple([int(num) for num in line[1].split(',')])
            data[i] = (line[0], sizes)
    return data

def count_arrangements(data, factor=1):
    def dp(i,j,curr_len,memo):
        # memo
        if (i,j,curr_len) in memo: return memo[(i,j,curr_len)]
        # base case: end of string and end of sizes
        if i >= len(groups):
            return 1 if i >= len(groups) and j >= len(sizes) else 0
        count = 0
        options = '#.' if groups[i] == '?' else groups[i]
        # recurses over both '#' and '.' if groups[i] == '?'
        for option in options:
            # continue current group
            if option == '#':
                count += dp(i+1, j, curr_len+1,memo)
            # end recent group, move on to next group
            elif option == '.':
                if curr_len:
                    # if we curr_len is large enough to be a group of springs, dp to next group
                    if j < len(sizes) and curr_len == sizes[j]:
                        count += dp(i+1, j+1,0,memo)
                # was not in a contiguous group, try again
                else:
                    count += dp(i+1, j,0,memo)
        memo[(i,j,curr_len)] = count
        return memo[(i,j,curr_len)]
    # 
    count = 0
    for groups, sizes in data:
        groups, sizes, memo = '?'.join([groups]*factor) + '.', sizes*factor, {}
        count += dp(0,0,0,memo)
    return count

data = parse_data(file)
# part one
print(f"The total sum of possible arrangements for each row is {count_arrangements(data, 1)}.")
# The total sum of possible arrangements for each row is 7084.

# part two
print(f"The total sum of possible arrangements for each row is {count_arrangements(data, 5)}.")
# The total sum of possible arrangements for each row is 8414003326821.s
