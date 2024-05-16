### Advent of Code - Day 17 - Part 2 ###

### Importing Packets
from functools import reduce

### Defining Classes
class PowerSource():

    DEBUG = True

    def __init__(self):
        self.cubes = []
        self.turnNum = 0
    
    def newCube(self, x, y, z, w):
        self.cubes.append(Cube(x, y, z, w))

    def boot(self):
        self.runTurns(6)

    def runTurns(self, num):
        for _ in range(num):
            self.runTurn()

    def runTurn(self):
        nextState = []

        ### Keeping Cubes Active
        for active in self.cubes:
            numNeighbors = self._numActiveAroundCube(active)
            if numNeighbors == 2 or numNeighbors == 3:
                nextState.append(active)
        
        ### Making Inactive Cubes Active
        neighbors = []
        for active in self.cubes:
            for coordinate in active.neighbors:
                ### BUGSSSSS YUCK
                #if coordinate not in neighbors:
                coordinateFound = False
                for other in neighbors:
                    if reduce(lambda x, y : x and y, map(lambda x, y: x == y, coordinate, other), True):
                        coordinateFound = True
                if not coordinateFound:
                    neighbors.append(coordinate)
        for neighbor in neighbors:
            inactive = True
            for cube in self.cubes:
                if cube.x == neighbor[0] and cube.y == neighbor[1] and cube.z == neighbor[2] and cube.w == neighbor[3]:
                    inactive = False
            if inactive:
                newCube = Cube(neighbor[0], neighbor[1], neighbor[2], neighbor[3])
                if self._numActiveAroundCube(newCube) == 3:
                    nextState.append(newCube)
        
        self.cubes = nextState
        self.turnNum += 1

        if PowerSource.DEBUG: print(self)

    def _getRow(self, z, w):
        output = ""
        minx, maxx = self.xMinMax
        miny, maxy = self.yMinMax
        cubes = []
        for cube in self.cubes:
            if cube.z == z and cube.w == w:
                cubes.append(cube)
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                cubeFound = False
                for cube in cubes:
                    if cube.x == x and cube.y == y:
                        cubeFound = True
                if cubeFound:
                    output += "#"
                else:
                    output += "."
            output += "\n"
        return output

    def _numActiveAroundCube(self, cube):
        numActive = 0
        for coordinate in cube.neighbors:
            if self._isActiveCube(coordinate[0], coordinate[1], coordinate[2], coordinate[3]):
                numActive += 1
        return numActive
    
    def _isActiveCube(self, x, y, z, w):
        active = False
        for cube in self.cubes:
            if cube.x == x and cube.y == y and cube.z == z and cube.w == w:
                active = True
        return active
    
    @property
    def numCubes(self):
        return len(self.cubes)
    
    @property
    def xMinMax(self):
        x = []
        for cube in self.cubes:
            x.append(cube.x)
        return min(x), max(x)
    
    @property
    def yMinMax(self):
        y = []
        for cube in self.cubes:
            y.append(cube.y)
        return min(y), max(y)
    
    @property
    def zMinMax(self):
        z = []
        for cube in self.cubes:
            z.append(cube.z)
        return min(z), max(z)
    
    @property
    def wMinMax(self):
        w = []
        for cube in self.cubes:
            w.append(cube.w)
        return min(w), max(w)

    def __repr__(self):
        output = f"\n\nTurn = {self.turnNum}\n\n"
        minz, maxz = self.zMinMax
        minw, maxw = self.wMinMax
        for z in range(minz, maxz + 1):
            for w in range(minw, maxw + 1):
                output += f"z={z}\nw={w}\n{self._getRow(z, w)}\n"
        return output

class Cube():
    def __init__(self, x, y, z, w):
        self._x = x
        self._y = y
        self._z = z
        self._w = w
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z
    
    @property
    def w(self):
        return self._w
    
    @property
    def neighbors(self):
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if x != 0 or y != 0 or z != 0 or w != 0:
                            neighbors.append([self._x + x, self._y + y, self._z + z, self._w + w])
        return neighbors
    
    def __repr__(self):
        return f"({self._x}, {self._y}, {self._z}, {self._w})"

### Defining Subroutines
def createPowerSource(myInput):
    myPowerSource = PowerSource()
    for y, row in enumerate(myInput.splitlines()):
        for x, item in enumerate([letter for letter in row]):
            if item == "#":
                myPowerSource.newCube(x, y, 0, 0)
    return myPowerSource

def main(myInput):
    myPowerSource = createPowerSource(myInput)
    if PowerSource.DEBUG: print(myPowerSource)
    myPowerSource.boot()
    print(f"Number of Cubes: {myPowerSource.numCubes}")

### Name Guard
if __name__ == "__main__":
    myInput = """#.......
.#..#..#
....#.#.
.##..#.#
#######.
#...####
###.##..
.##.#.#."""
    main(myInput)
