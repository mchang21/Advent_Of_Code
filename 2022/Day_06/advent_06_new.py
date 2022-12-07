PATH = '../Advent_Of_Code/2022/Day_06/'

def parse_data(file):
    with open(file) as f:
        input = f.readline()
    return input.rstrip()

datastream = parse_data(PATH + 'input06.txt')

# part one and two
def process_datastream(datastream, max_len):

    for i in range(len(datastream)-max_len):
        if len(set(datastream[i:i+max_len])) == max_len:
            return i + max_len


print(f"{process_datastream(datastream, 4)} characters need to be processed before the first start-of-packet marker is detected")
# Output: 1080 characters need to be processed before the first start-of-packet marker is detected

print(f"{process_datastream(datastream, 14)} characters need to be processed before the first start-of-message marker is detected")
# Output: 3645 characters need to be processed before the first start-of-message marker is detected