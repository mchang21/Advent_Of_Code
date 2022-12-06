PATH = '../Advent2022/2022/Day_04/'

# part one
def find_overlapping_pairs(file):
    overlap = 0

    with open(file) as f:
        for assignments in f:
            elf_one_start, elf_one_end, elf_two_start, elf_two_end = assignments.split('\n')[0].replace('-',',').split(',')
            elf_one_start, elf_one_end, elf_two_start, elf_two_end = int(elf_one_start), int(elf_one_end), int(elf_two_start), int(elf_two_end)

            # elf one essignments are fully contained by elf two assignments
            if (elf_one_start >= elf_two_start) and (elf_one_end <= elf_two_end):
                overlap += 1

            # elf two assignments are fully contained by elf one assignments
            elif (elf_two_start >= elf_one_start) and (elf_two_end <= elf_one_end):
                overlap += 1

    return overlap

print(f"The number of assignment pairs where one range fully contains the other is {find_overlapping_pairs(PATH + 'input04.txt')}")
# Output: The number of assignment pairs where one range fully contains the other is 424

# part two
def find_any_overlapping_pairs(file):
    overlap = 0

    with open(file) as f:
        for assignments in f:
            elf_one_start, elf_one_end, elf_two_start, elf_two_end = assignments.split('\n')[0].replace('-',',').split(',')
            elf_one_start, elf_one_end, elf_two_start, elf_two_end = int(elf_one_start), int(elf_one_end), int(elf_two_start), int(elf_two_end)

            # elf one essignments overlap with elf two assignments
            if (elf_two_start >= elf_one_start) and (elf_two_start <= elf_one_end):
                overlap += 1

            # elf two assignments overlap with elf one assignments
            elif (elf_one_start >= elf_two_start) and (elf_one_start <= elf_two_end):
                overlap += 1

    return overlap
    
print(f"The number of assignment pairs where there is any overlap is {find_any_overlapping_pairs(PATH + 'input04.txt')}")
# Output: The number of assignment pairs where there is any overlap is 804