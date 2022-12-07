PATH = '../Advent_Of_Code/2022/Day_06/'

def parse_data(file):
    with open(file) as f:
        input = f.readline()
    return input.rstrip()

datastream = parse_data(PATH + 'input06.txt')

# part one and two
def process_datastream(datastream, max_len):
    window = dict()
    start = 0

    for end in range(len(datastream)-max_len):
        # check if the index is a start-of marker
        if len(window) == max_len:
            return end

        # add letter
        window[datastream[end]] = window.get(datastream[end], 0) + 1

        # remove letter from the beginning of the window
        if end-start >= max_len:
            if window[datastream[start]] == 1:
                del window[datastream[start]]
            else:
                window[datastream[start]] -= 1
            start += 1

print(f"{process_datastream(datastream, 4)} characters need to be processed before the first start-of-packet marker is detected")
# Output: 1080 characters need to be processed before the first start-of-packet marker is detected

print(f"{process_datastream(datastream, 14)} characters need to be processed before the first start-of-message marker is detected")
# Output: 3645 characters need to be processed before the first start-of-message marker is detected