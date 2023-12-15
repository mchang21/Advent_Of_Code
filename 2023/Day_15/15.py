import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split(',')
    return data

def hash(s):
    val = 0
    for c in s:
        # increaase current value by curr ascii char
        val += ord(c)
        # set the current value to itself multiplied by 17
        val *= 17
        # set the current value to the remainder of dividing itself by 256
        val %= 256
    return val

def sum_hash(data):
    return sum(hash(d) for d in data)

data = parse_data(file)
# part one
print(f"The sum of running the HASH algorithm on each step is {sum_hash(data)}.")
# The sum of running the HASH algorithm on each step is 519041.

# part two

def get_boxes(data):
    boxes = [[] for _ in range(256)]
    for d in data:
        if d[-1] == '-':
            label = d[:-1]
            box_index, remove_index = hash(label), None
            # search for label to remove
            for i, box in enumerate(boxes[box_index]):
                if label == box[0]:
                    remove_index = i
                    break
            # if we found a label to remove, remove it
            if remove_index is not None:
                boxes[box_index].pop(remove_index)
        else:
            label, focal_length = d.split('=')
            box_index, found = hash(label), False
            # replace lens
            for i, box in enumerate(boxes[box_index]):
                if box[0] == label:
                    box[1] = int(focal_length)
                    found = True
                    break
            # add lens
            if not found:
                boxes[box_index].append([label, int(focal_length)])
    return boxes

def sum_focusing_power(boxes):
    total_focusing_power = 0
    for box_num, box in enumerate(boxes):
        for i, (_, focal_length) in enumerate(box):
            total_focusing_power += (box_num+1) * (i+1) * focal_length
    return total_focusing_power

# part two
print(f"The total focusing power of the lens configuration is {sum_focusing_power(get_boxes(data))}.")
# The total focusing power of the lens configuration is 260530.