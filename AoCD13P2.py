### Advent of Code - Day 13 - Part 2 ###

### Importing Packets
from functools import reduce

### Defining Classes
class Series():
    def __init__(self, a, d):
        self.a = a
        self.d = d
    
    @property
    def firstValue(self):
        return self.a
    
    def hasValue(self, value):
        value += -self.a
        return value % self.d == 0

    def __repr__(self):
        if self.a == 0:
            return f"{self.d}n"
        else:
            return f"{self.d}n + {self.a}"

### Defining Subroutines
def handleInput(myInput):
    output = []
    _, busses = myInput.splitlines()
    busses = busses.split(",")
    for index in range(len(busses)):
        if busses[index] != "x":
            output.append(Series(-index, int(busses[index])))
    return output

def combineSeries(ser1, ser2):
    return Series(firstIntersection(ser1, ser2), ser1.d * ser2.d)

def firstIntersection(ser1, ser2):
    value = ser1.a
    while True:
        if ser2.hasValue(value):
            break
        value += ser1.d
    return value

def main(myInput):
    busses = handleInput(myInput)
    print(reduce(combineSeries, busses).firstValue)

### Name Guard
if __name__ == "__main__":
    myInput = """1001171
17,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,13"""
    main(myInput)
