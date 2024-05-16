### Advent of Code - Day 10 - Part 1 ###

### Defining Subroutines
def calculateDifference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def main(myInput):
    myInput = sorted(list(map(int, myInput.splitlines())))
    diff1 = 1
    diff3 = 1
    for index in range(0, len(myInput) - 1):
        diff = calculateDifference(myInput[index], myInput[index + 1])
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
    print(diff1)
    print(diff3)
    print(diff1 * diff3)

### Name Guard
if __name__ == "__main__":
    myInput = """86
149
4
75
87
132
12
115
62
61
153
78
138
43
88
108
59
152
109
63
42
60
7
104
49
156
35
2
52
72
125
94
46
136
26
16
76
117
116
150
20
13
141
131
127
67
3
40
54
82
36
100
41
56
146
157
89
23
8
55
111
135
144
77
124
18
53
92
126
101
69
27
145
11
151
31
19
34
17
130
118
28
107
137
68
93
85
66
97
110
37
114
79
121
1"""
    main(myInput)
