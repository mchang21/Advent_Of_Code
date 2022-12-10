import math

PATH = '../Advent_Of_Code/2022/Day_09/'

def parse_data(file):
    directions = []
    with open(file) as f:
        for line in f:
            dir,num = line.strip().split(' ')
            directions.append([dir, int(num)])
    return directions

class Rope:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move(self, direction):
        # move right
        if direction == 'R':
            self.move_right()
        # move left
        elif direction == 'L':
            self.move_left()
        # move up
        elif direction == 'U':
            self.move_up()
        # move down
        else:
            self.move_down()

    def update_rope(self, x, y):
        max_dist = 2
        if math.dist([self.x,self.y], [x,y]) >= max_dist:
            dx, dy = x-self.x, y-self.y
            if dx > 0:
                self.move_right()
            elif dx < 0:
                self.move_left()
            if dy > 0:
                self.move_up()
            elif dy < 0:
                self.move_down()
        return

    @staticmethod
    def simulate_moves(directions, num_knots=2):
        rope = [Rope() for _ in range(num_knots)]
        visited = set()

        for direction, amount in directions:
            for _ in range(amount):
                # move the head
                rope[0].move(direction)
                # update the location of each knot
                for i in range(1, len(rope)):
                    rope[i].update_rope(rope[i-1].x, rope[i-1].y)
                # add location of the tail
                visited.add((rope[-1].x,rope[-1].y))

        return len(visited)

rope = Rope()
directions = parse_data(PATH + 'input.txt')
# directions = parse_data(PATH + 'example.txt')
# part one
print(f"The number of positions the tail visits at least once is {rope.simulate_moves(directions, 2)}")
# part two
print(f"The number of positions the tail visits at least once is {rope.simulate_moves(directions, 10)}")
