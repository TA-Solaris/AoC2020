### Advent of Code - Day 15 - Part 1 ###

### Defining Subroutines
def runTest(num, mem, turnNum):
    if num in mem.keys():
        output = turnNum - mem[num]
    else:
        output = 0
    mem[num] = turnNum
    return output

def main(myInput):
    memory = {}
    turn = 1
    for num in list(map(int, myInput.split(","))):
        nextNum = runTest(num, memory, turn)
        turn += 1
    while turn != 2020:
        nextNum = runTest(nextNum, memory, turn)
        turn += 1
    print(nextNum)

### Name Guard
if __name__ == "__main__":
    myInput = """9,19,1,6,0,5,4"""
    main(myInput)
