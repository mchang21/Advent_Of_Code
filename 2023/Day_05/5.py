PATH = '../Advent_Of_Code/2023/Day_05/'

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().split("\n\n")
        # parse seeds
        data[0] = [int(num) for num in data[0].split(':')[1].strip().split()]
        # parse mappings
        for i in range(1, len(data)):
            data[i] = [[int(num) for num in values.split()] for values in data[i].split('\n')[1:]]
    return data

# part one
def get_lowest_location_num(data):
    seeds = data[0]
    lowest_location = float('inf')
    # iterate beginning with each seed
    for seed in seeds:
        # iterate over each mapping
        for mapping in data[1:]:
            # check each potential range if `seed` fits within the range
            for dest_start, src_start, range_length in mapping:
                if src_start <= seed < src_start + range_length:
                    # set seed as the next starting point
                    seed = dest_start + (seed - src_start)
                    break
        # keep track of the lowest location
        lowest_location = min(lowest_location, seed)
    # return the lowest location number corresponding to the initial seeds
    return lowest_location

data = parse_data(PATH + "input.txt")

# part one
print(f"The lowest location number corresponding to any of the initial seeds is {get_lowest_location_num(data)}.")

# part two

# get range of each of the seeds
def get_seed_ranges(seeds):
    # [inclusive, exclusive]
    return [(seeds[i],seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

# get lowest location given range of seeds
def get_lowest_location_num_after_ranges(data):
    seed_ranges = get_seed_ranges(data[0])

    for mapping in data[1:]:
        mapped_seed_ranges = []
        for seed_range in seed_ranges:
            seed_start, seed_end = seed_range
            range_mapped = False

            for dest_start, src_start, range_length in mapping:
                # get the overlap range
                overlap_start = max(seed_start, src_start)
                overlap_end = min(seed_end, src_start+range_length)
                # valid overlap range
                if overlap_start < overlap_end:
                    mapped_seed_ranges.append((overlap_start-src_start+dest_start, overlap_end - src_start + dest_start))

                    if seed_start < overlap_start:
                        seed_ranges.append((seed_start, overlap_start))
                    if overlap_end < seed_end:
                        seed_ranges.append((overlap_end, seed_end))
                    range_mapped = True

                    break
            if not range_mapped:
                mapped_seed_ranges.append((seed_start, seed_end))
        seed_ranges = mapped_seed_ranges

    return min(seed_ranges)[0]

# part two
print(f"The lowest location number which corresponds to any of the initial seed numbers is {get_lowest_location_num_after_ranges(data)}.")

