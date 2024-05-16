### Advent of Code - Day 13 - Part 1 ###

### Defining Subroutines
def getNextBus(myTime, busses):
    start = myTime
    while True:
        for bus in busses:
            if start % bus == 0:
                return start - myTime, bus
        start += 1

def main(myInput):
    myTime, busses = myInput.splitlines()
    myTime = int(myTime)
    busses = list(map(int, list(filter(lambda a: a != "x", busses.split(",")))))
    timeToWait, busID = getNextBus(myTime, busses)
    print(timeToWait * busID)

### Name Guard
if __name__ == "__main__":
    myInput = """1001171
17,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,13"""
    main(myInput)
