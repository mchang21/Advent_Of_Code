PATH = '../Advent_Of_Code/2021/Day_03/'

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

data = parse_data(PATH + "input03.txt")
# remove newline character
for i in range(len(data)):
    data[i] = data[i].rstrip()

# part one
def find_gamma_and_epsilon(data):
    n = len(data)
    bit_count = [0 for _ in range(len(data[0]))]
    gamma_rate = ""
    epsilon_rate = ""

    for d in data:
        # count number of 1 bits in each position
        for i in range(len(d)):
            bit = int(d[i])
            if bit:
                bit_count[i] += 1

    # get gamma rate and epsilon rate from bit_count
    for count in bit_count:
        # if 1 is the most common bit
        if count > n-count:
            gamma_rate += "1"
            epsilon_rate += "0"
        # if 0 is the most common bit
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

print(f"The power consumption of the submarine is {find_gamma_and_epsilon(data)}")
# Output: The power consumption of the submarine is 3687446

# part two
def find_life_support_rating(data):
    o2_data = data.copy()
    co2_data = data.copy()

    index = 0
    # find the oxygen generator rating
    while len(o2_data) > 1:
        most_common_bit = find_most_common_bit(o2_data, index)
        o2_data = list(filter(lambda x: x[index] == most_common_bit, o2_data))
        index += 1

    index = 0
    # find the co2 scrubber rating
    while len(co2_data) > 1:
        least_common_bit = find_least_common_bit(co2_data, index)
        co2_data = list(filter(lambda x: x[index] == least_common_bit, co2_data))
        index += 1

    # convert to int from binary
    o2_generator_rating = int(o2_data[0], 2)
    co2_scrubber_rating = int(co2_data[0], 2)
    
    return o2_generator_rating * co2_scrubber_rating

# finds the most common bit for a given index
def find_most_common_bit(data, index):
    n = len(data)
    one_count = 0
    for d in data:
        if d[index] == "1":
            one_count += 1
    
    return "1" if one_count >= n - one_count else "0"

# finds the least common bit for a given index
def find_least_common_bit(data, index):
    n = len(data)
    one_count = 0
    for d in data:
        if d[index] == "1":
            one_count += 1
    
    return "0" if one_count >= n - one_count else "1"

print(f"The life support rating of the submarine is {find_life_support_rating(data)}")
# Output: The life support rating of the submarine is 4406844