### Advent of Code - Day 20 - Part 1 ###

### Importing Packets
from functools import reduce

### Defining Exceptions
class TileError(Exception):
    pass

### Defining Classes
class Tile():
    def __init__(self, tileData):
        tileData = tileData.splitlines()
        self.ID = int(tileData[0][5:9])
        self.data = [[letter for letter in line] for line in tileData[1:]]

    def getEdge(self, edgeNum, reflected):
        if reflected:
            if edgeNum == 1:
                return reversed(self.edge1)
            elif edgeNum == 2:
                return reversed(self.edge2)
            elif edgeNum == 3:
                return reversed(self.edge3)
            elif edgeNum == 4:
                return reversed(self.edge4)
        else:
            if edgeNum == 1:
                return self.edge1
            elif edgeNum == 2:
                return self.edge2
            elif edgeNum == 3:
                return self.edge3
            elif edgeNum == 4:
                return self.edge4
        raise TileError(f"Your entered edge -  num: {edgeNum} ref: {reflected}  - was invalid. ")

    @property
    def edge1(self):
        return [line[0] for line in self.data]
    
    @property
    def edge2(self):
        return self.data[0]
    
    @property
    def edge3(self):
        return [line[-1] for line in self.data]
    
    @property
    def edge4(self):
        return self.data[0]

class Sherlock_GreatSolverOfThings():
    def __init__(self, tiles):
        self.connections = {}
        for tile in tiles:
            self.connections[tile.ID] = []
        self.findConnections(tiles)
        self.reduceConnections()

    def compareEdges(self, a, b):
        return reduce(lambda x, y : x and y, map(lambda x, y: x == y, a, b), True)

    def findConnections(self, tiles):
        for tile1 in tiles:
            for tile2 in tiles:
                if tile1 != tile2:
                    for edge1 in range(1, 5):
                        for edge2 in range(1, 5):
                            for reverse1 in range(0, 2):
                                for reverse2 in range(0, 2):
                                    if self.compareEdges(tile1.getEdge(edge1, reverse1 == 0), tile2.getEdge(edge2, reverse2 == 0)):
                                        self.connections[tile1.ID].append([tile2.ID, edge1, reverse1 == 0])
                                        self.connections[tile2.ID].append([tile1.ID, edge2, reverse2 == 0])
    
    def reduceConnections(self):
        while True:
            for key, value in self.connections.items():
                nums = [0, 0, 0, 0]
                for connection in value:
                    nums[connection[1] - 1] += 1
                for edge, value in enumerate(nums):
                    edge += 1
                    if value == 1:
                        print("no definite edges... i am so sad, why is there so much suffering")

### Defining Subroutines
def getTiles(myInput):
    tiles = []
    for tile in myInput.split("\n\n"):
        tiles.append(Tile(tile))
    return tiles

def main(myInput):
    tiles = getTiles(myInput)
    mySherlock = Sherlock_GreatSolverOfThings(tiles)

### Name Guard
if __name__ == "__main__":
    myInput = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
    main(myInput)
