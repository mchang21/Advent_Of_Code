PATH = '../Advent_Of_Code/2023/Day_06/'

def parse_data(file):
    with open(file, 'r') as f:
        raw_data = f.read().strip()
        data = raw_data.split('\n')
        for i in range(len(data)):
            data[i] = [int(num) for num in data[i].split(':')[1].strip().split()]
    return data

# use binary search to find the lower bound (least amount of time I can hold and still win)
# and find the upper bound (most amount of time I can hold and still win)
def ways_to_beat_record(time, record):
    # binary search to find the lower bound
    l, r = 1, time
    while l <= r:
        mid = l + ((r-l) // 2)
        speed, time_left = mid, time - mid
        distance_travelled = speed*time_left
        if distance_travelled >= record:
            r = mid-1
        else:
            l = mid + 1
    lower_bound = l

    # binary search again to find the upper bound
    l, r = 1, time
    while l <= r:
        mid = l + ((r-l) // 2)
        speed, time_left = mid, time - mid
        distance_travelled = speed*time_left
        if distance_travelled >= record:
            l = mid + 1
        else:
            r = mid - 1
    upper_bound = l
    
    return upper_bound - lower_bound

# function to calculate the product of ways that can beat the record
def product_of_ways_to_beat_record(data):
    prod = 1
    for time, record in zip(data[0], data[1]):
        prod *= ways_to_beat_record(time, record)
    return prod

data = parse_data(PATH + "input.txt")
# part one
print(f"The product of ways to beat the record is {product_of_ways_to_beat_record(data)}.")
# The product of ways to beat the record is 1731600.
    
# part two
def ways_to_beat_record_in_longer_race(data):
    time, record = "", ""
    # convert the separate times and records into one big number
    for t, r in zip(data[0], data[1]):
        time += str(t)
        record += str(r)
    return ways_to_beat_record(int(time), int(record))

# part two
print(f"The number of ways to beat the record in the much longer race is {ways_to_beat_record_in_longer_race(data)}.")
# The number of ways to beat the record in the much longer race is 40087680.


