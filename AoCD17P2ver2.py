### Advent of Code - Day 17 - Part 2 ###

### Importing Packets
from functools import reduce

### Defining Classes
class PowerSource():

    DEBUG = True

    def __init__(self, myInput):
        self.cubes = [False for _ in range(100000000)]
        self.actives = []
        self.turnNum = 0

        self.build(myInput)
    
    def build(self, myInput):
        for y, row in enumerate(myInput.splitlines()):
            for x, item in enumerate([letter for letter in row]):
                if item == "#":
                    self.setCube(self.cubes, self.actives, x, y, 0, 0, True)
        print("Build Complete")
    
    def getCube(self, x, y, z, w):
        if x < 0: x += 100
        if y < 0: y += 100
        if z < 0: z += 100
        if w < 0: w += 100
        return self.cubes[int(f"{str(x).zfill(2)}{str(y).zfill(2)}{str(z).zfill(2)}{str(w).zfill(2)}")]

    def setCube(self, cubes, actives, x, y, z, w, value):
        tx, ty, tz, tw = x, y, z, w
        if tx < 0: tx += 100
        if ty < 0: ty += 100
        if tz < 0: tz += 100
        if tw < 0: tw += 100
        cubes[int(f"{str(tx).zfill(2)}{str(ty).zfill(2)}{str(tz).zfill(2)}{str(tw).zfill(2)}")] = value
        if value: actives.append([x, y, z, w])
    
    def getNeighbours(self, x, y, w, z):
        neighbors = []
        for tx in range(-1, 2):
            for ty in range(-1, 2):
                for tz in range(-1, 2):
                    for tw in range(-1, 2):
                        if tx != 0 or ty != 0 or tz != 0 or tw != 0:
                            neighbors.append([x + tx, y + ty, z + tz, w + tw])
        return neighbors
    
    def getNumNeighbours(self, x, y, z, w):
        count = 0
        for neighbor in self.getNeighbours(x, y, w, z):
            if self.getCube(neighbor[0], neighbor[1], neighbor[2], neighbor[3]): count += 1
        return count

    def boot(self):
        self.runTurns(6)

    def runTurns(self, num):
        for _ in range(num):
            self.runTurn()

    def runTurn(self):
        cubes = self.cubes.copy()
        actives = []

        for cube in self.actives:
            ### Checking the cube to remain active
            num = self.getNumNeighbours(cube[0], cube[1], cube[2], cube[3])
            if num == 2 or num == 3:
                self.setCube(cubes, actives, cube[0], cube[1], cube[2], cube[3], True)
            else:
                self.setCube(cubes, actives, cube[0], cube[1], cube[2], cube[3], False)
            
            ### Checking cubes to turn active
            for neighbor in self.getNeighbours(cube[0], cube[1], cube[2], cube[3]):
                if not self.getCube(neighbor[0], neighbor[1], neighbor[2], neighbor[3]):
                    if self.getNumNeighbours(neighbor[0], neighbor[1], neighbor[2], neighbor[3]) == 3:
                        self.setCube(cubes, actives, neighbor[0], neighbor[1], neighbor[2], neighbor[3], True)
        
        self.cubes = cubes
        self.actives = actives
        self.turnNum += 1
        print(f"Turn {self.turnNum} Complete!")
    
    @property
    def numCubes(self):
        return len(self.actives)
        
### Defining Subroutines
def main(myInput):
    myPowerSource = PowerSource(myInput)
    myPowerSource.boot()
    print(f"Number of Cubes: {myPowerSource.numCubes}")

### Name Guard
if __name__ == "__main__":
    myInput = """.#.
..#
###"""
    main(myInput)
