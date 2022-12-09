from collections import defaultdict

PATH = '../Advent_Of_Code/2022/Day_07/'

class Directory:
    def __init__(self, directory=None):
        self.parent = None
        self.directory = directory
        self.subdirectories = defaultdict(Directory)
        self.files = []
        self.size = 0
        return

    # parses command lines to recreate the filesystem structure
    def parse_commands(self, file):
        current_directory = self
        current_parent_directory = None

        with open(file) as f:
            for line in f:
                # start creating tree/filesystem structure
                command = line.replace('$', ' ').strip().split(' ')

                if command[0] == 'ls': continue
                elif command[0] == 'cd':
                    # go up the tree
                    if command[1] == '..':
                        current_directory = current_directory.parent
                        current_parent_directory = current_directory # update current parent
                    # traverse to directory
                    else:
                        # add the root directory
                        if not current_directory.directory:
                            current_directory.directory = command[1]
                        # add every other directory
                        else:
                            current_directory = current_directory.subdirectories[command[1]]
                            current_directory.directory = command[1] # add directory
                        # set parent directory
                        current_directory.parent = current_parent_directory # set its parent
                        current_parent_directory = current_directory # save new parent

                # add to list of subdirectories
                elif command[0] == 'dir':
                    current_directory.subdirectories[command[1]] = Directory(command[1])
                # add size of files to the size of the directory
                # add file to list of files
                else:
                    current_directory.size += int(command[0])
                    current_directory.files.append((command[1], command[0]))
        return

    # recursive function to update the size of the current directory to include
    # the size of its subdirectories
    def update_total_size(self):
        if len(self.subdirectories) == 0:
            return self.size
        
        local_sum = 0
        for subdir in self.subdirectories:
            local_sum += self.subdirectories[subdir].update_total_size()

        self.size += local_sum
        return self.size

    # DFS to get the size of all directories <= max_size
    def get_total_size(self, max_size):
        stack = [self]
        total_size = 0
        # DFS
        while stack:
            directory = stack.pop()
            # add to total size
            if directory.size <= max_size:
                total_size += directory.size

            # add neighbors to stack
            for subdir in directory.subdirectories:
                stack.append(directory.subdirectories[subdir])
        return total_size

    # DFS to find the smallest directory that would free up enough space
    # on the file system to run the update
    def find_directory_to_delete(self, update_size):
        TOTAL_DISK_SPACE = 70_000_000
        minimum_size = update_size - (TOTAL_DISK_SPACE - self.size) # update_size - unused_space

        directory_to_delete = self
        stack = [self]
        # DFS
        while stack:
            directory = stack.pop()
            # choose the smaller directory whose size meets the minimum_size
            if directory.size >= minimum_size and directory.size < directory_to_delete.size:
                directory_to_delete = directory

            # add neighbors to stack
            for subdir in directory.subdirectories:
                stack.append(directory.subdirectories[subdir])

        return directory_to_delete


filesystem = Directory()
filesystem.parse_commands(PATH + 'input07.txt')
filesystem.update_total_size()

# part one
print(f"The sum of directories with a total size of at most 100,000 is {filesystem.get_total_size(100_000)}")
# Output: The sum of directories with a total size of at most 100,000 is 2061777

# part two
directory_to_delete = filesystem.find_directory_to_delete(30_000_000)
print(f"The smallest directory that can be deleted is directory '{directory_to_delete.directory}' with size {directory_to_delete.size}")
# Output: The smallest directory that can be deleted is directory 'vtnptsl' with size 4473403