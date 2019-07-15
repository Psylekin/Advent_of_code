def connection_test():
    return 1

def loadData(location):
    with open(location) as input:
        return input.read().split()
def parse(it):
    # read the number of children and number of metadata
    num_children, num_metadata = next(it), next(it)
    # recursively parse children nodes
    children = [parse(it) for _ in range(num_children)]
    # read the metadata
    metadata = [next(it) for _ in range(num_metadata)]
    return (metadata, children)

# Wow, cool solution!

data = loadData("advent_of_code/7/project/input.txt")

root = parse(map(int, data))
print(root)