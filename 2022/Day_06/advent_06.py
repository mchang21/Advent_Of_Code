PATH = '../Advent_Of_Code/2022/Day_06/'

def parse_data(file):
    with open(file) as f:
        input = f.readline()
    return input.rstrip()

datastream = parse_data(PATH + 'input06.txt')

# part one
def process_packet(datastream):
    window = dict()

    # initial window
    for i in range(3):
        window[datastream[i]] = window.get(datastream[i], 0) + 1

    for i in range(3, len(datastream)):
        # add the letter at i
        window[datastream[i]] = window.get(datastream[i], 0) + 1

        # check if the index is a start-of-packet marker
        if len(window) == 4:
            return i+1

        # remove letter from the beginning of the window
        if window[datastream[i-3]] == 1:
            del window[datastream[i-3]]
        else:
            window[datastream[i-3]] -= 1

print(f"{process_packet(datastream)} characters need to be processed before the first start-of-packet marker is detected")
# Output: 1080 characters need to be processed before the first start-of-packet marker is detected

# part two
def process_message(datastream):
    window = dict()

    # initial window
    for i in range(13):
        window[datastream[i]] = window.get(datastream[i], 0) + 1

    for i in range(13, len(datastream)):
        # add the letter at i
        window[datastream[i]] = window.get(datastream[i], 0) + 1

        # check if the index is a start-of-packet marker
        if len(window) == 14:
            return i+1

        # remove letter from the beginning of the window
        if window[datastream[i-13]] == 1:
            del window[datastream[i-13]]
        else:
            window[datastream[i-13]] -= 1

    return

print(f"{process_message(datastream)} characters need to be processed before the first start-of-message marker is detected")
# Output: 3645 characters need to be processed before the first start-of-message marker is detected