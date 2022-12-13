PATH = '../Advent_Of_Code/2022/Day_10/'

# part one
def calculate_signal_strength(file):
    cycle, signal_strength, reg_x = 0, 0, 1

    with open(file) as f:
        for line in f:
            command = line.strip().split(' ')

            if command[0] == "noop":
                for _ in range(1):
                    cycle += 1
                    # check the cycle to determine signal strength
                    if cycle == 20 or (cycle - 20) % 40 == 0:
                        signal_strength += cycle * reg_x

            elif command[0] == "addx":
                for _ in range(2):
                    cycle += 1
                    # check cycle to determine signal strength
                    if cycle == 20 or (cycle - 20) % 40 == 0:
                        signal_strength += cycle * reg_x
                # at the end of execution, add to reg_x
                reg_x += int(command[1])

    return signal_strength

# part two
def draw_crt(file):
    pixels = [['.' for _ in range(40)] for _ in range(6)]
    row, position, sprite = 0, 0, 1

    with open(file) as f:
        for line in f:
            command = line.strip().split(' ')
            
            if command[0] == "noop":
                for _ in range(1):
                    # check if the pixel being drawn overlaps with the sprite
                    if position in [sprite - 1, sprite, sprite + 1]:
                        pixels[row][position] = '#'

                    # update position
                    position += 1
                    if position % 40 == 0:
                        position = 0
                        row += 1

            elif command[0] == "addx":
                for _ in range(2):
                    # check if the pixel being drawn overlaps with the sprite
                    if position in [sprite - 1, sprite, sprite + 1]:
                        pixels[row][position] = '#'
                    
                    # update position
                    position += 1
                    if position % 40 == 0:
                        position = 0
                        row += 1

                # at the end of execution, add to reg_x
                sprite += int(command[1])

    return pixels

# part one 
print(f"The signal strength after 220 cycles is {calculate_signal_strength(PATH + 'input.txt')}\n")

# part two
pixels = draw_crt(PATH + "input.txt")
# draw_crt(PATH + "example.txt")
print("After drawing the CRT, the following letters we get are:\n")
for row in pixels:
    print(''.join(row))