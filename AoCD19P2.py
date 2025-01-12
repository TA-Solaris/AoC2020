### Advent of Code - Day 19 - Part 2 ###

# Answer upper bound == 411
# Answer lower bound == 407
# regex is ^(((a)(((a)((a)((((a)(a))(b)|((b)(b)|(a)(a))(a))(a)|((((a)|(b))(b)|(a)(a))((a)|(b)))(b))|(b)((((b)(b))(a))(b)|(((a)(a)|(a)(b))(b)|((b)(b)|(a)(a))(a))(a)))|(b)((b)((((a)((a)|(b))|(b)(a))(b)|((b)(b))(a))(b)|((((a)|(b))(b)|(a)(a))((a)|(b)))(a))|(a)((a)((a)((b)(a)|(a)(a))|(b)((a)((a)|(b))|(b)(a)))|(b)((b)(((a)|(b))((a)|(b)))|(a)((a)(a))))))(b)|((b)((a)(((a)((a)(a)|(a)(b))|(b)((a)(b)))(b)|((a)((a)(a)|(a)(b))|(b)((a)(a)))(a))|(b)(((((a)|(b))(b)|(a)(a))(a)|((b)(b)|(a)(b))(b))(a)|((a)((a)(b))|(b)((a)((a)|(b))|(b)(a)))(b)))|(a)(((a)((b)((a)((a)|(b))|(b)(a)))|(b)((b)((b)(b)|(a)(a))|(a)((a)(b))))(b)|((a)((b)(((a)|(b))(b)|(a)(a))|(a)((a)(a)|(a)(b)))|(b)(((a)(b)|(b)((a)|(b)))(b)))(a)))(a))|(b)(((a)(((((a)(a)|(a)(b))(a)|((a)(b))(b))(b)|((a)((a)(a)|(a)(b))|(b)((b)(a)|(a)(a)))(a))(b)|((b)((b)((b)(a)|(a)(a))|(a)((b)(b)))|(a)(((b)(a))(b)|((b)(b)|(a)(a))(a)))(a))|(b)((b)((b)(((b)(a)|(a)(b))(a)|((b)(b)|(a)(b))(b))|(a)(((a)(a)|(a)(b))(a)|((a)(a))(b)))|(a)((b)(((a)(b)|(b)((a)|(b)))((a)|(b)))|(a)((b)((a)(b)|(b)((a)|(b)))|(a)((b)(b)|(a)(a))))))(b)|(((a)(((((a)|(b))((a)|(b)))(a)|((a)(a)|(a)(b))(b))(a)|((a)((b)(a)|(a)(a))|(b)((a)(a)|(a)(b)))(b))|(b)((a)(((a)|(b))((b)(a)|(a)(b)))|(b)((a)((b)(a))|(b)((a)((a)|(b))|(b)(a)))))(b)|((((((a)|(b))((a)|(b)))(a)|((a)(a)|(a)(b))(b))(a)|((b)((b)(b))|(a)((b)(b)|(a)(b)))(b))(b)|((((b)(b))(b)|((b)(a)|(a)(b))(a))(a)|(((a)(b)|(b)((a)|(b)))(b)|((a)(b))(a))(b))(a))(a))(a)))+11)$

### Importing Packets
import re

### Defining Subroutines
def splitInput(myInput):
    myInput = myInput.splitlines()
    rules, tests = translateRules(myInput[:myInput.index("")]), myInput[myInput.index("") + 1:]
    return rules, tests

def translateRules(rules):
    newRules = {}

    ### Setting up Keys
    for rule in rules:
        key, value = rule.split(": ")
        value = "( " + value + " )"
        newRules[key] = value.replace('"', "")
    
    ### Fixing format
    #for key in newRules.keys():
    newRules["0"] = fixRule(newRules["0"], newRules)
    
    #for key in newRules.keys():
    newRules["0"] = "^" + newRules["0"] + "$"
    newRules["0"] = newRules["0"].replace(" ", "")
    
    return newRules

def fixRule(rule, rules):
    while True:
        running = False
        testRule = rule.split(" ")
        for letter in testRule:
            if isRule(letter) and letter != "11":
                if letter == "8":
                    rule = rule[:rule.find(letter)] +  "42 +" + rule[rule.find(letter) + len(letter):]
                elif letter == "11":
                    rule = rule[:rule.find(letter)] +  "42 + 31 +" + rule[rule.find(letter) + len(letter):]
                else:
                    rule = rule[:rule.find(letter)] +  rules[letter] + rule[rule.find(letter) + len(letter):]
                running = True
                break
        if not running:
            break
    return rule

def isRule(value):
    try:
        int(value)
        return True
    except:
        return False

def createRegExs(regEx, rules, num):
    exs = []
    rule42 = fixRule("42", rules).replace(" ", "")
    rule31 = fixRule("31", rules).replace(" ", "")
    for times in range(1, num + 1):
        exs.append(re.compile(regEx.replace("11", rule42*times + rule31*times)))
    return exs

def main(myInput):
    rules, tests = splitInput(myInput)
    exs = createRegExs(rules["0"], rules, 10)
    count = 0
    for test in tests:
        for _rex in exs:
            if _rex.match(test) is not None:
                count += 1
                break
    print(f"Total: {count}")

### Name Guard
if __name__ == "__main__":
    myInput = """12: "b"
120: 113 12 | 68 106
101: 12 12 | 106 12
104: 12 59 | 106 101
98: 12 78 | 106 125
87: 106 12 | 12 109
102: 12 95 | 106 71
27: 12 84 | 106 127
69: 68 106 | 101 12
75: 3 106 | 79 12
128: 12 74 | 106 17
0: 8 11
118: 12 113 | 106 101
122: 120 106 | 51 12
109: 106 | 12
97: 106 28 | 12 125
70: 106 28 | 12 34
82: 106 40 | 12 38
123: 83 12 | 85 106
129: 61 106 | 126 12
105: 106 37 | 12 47
86: 57 12 | 18 106
35: 12 87 | 106 78
42: 106 2 | 12 88
18: 12 76 | 106 67
45: 12 101 | 106 52
59: 109 12 | 106 106
55: 12 9 | 106 33
32: 12 115 | 106 35
54: 106 28 | 12 23
21: 106 82 | 12 102
33: 12 15 | 106 10
56: 106 1 | 12 98
110: 109 68
100: 80 12 | 58 106
24: 34 12 | 78 106
63: 12 72 | 106 32
13: 113 106 | 59 12
11: 42 31
60: 28 12 | 78 106
46: 107 12 | 89 106
107: 106 81 | 12 62
112: 106 101 | 12 4
124: 106 23 | 12 52
53: 56 12 | 90 106
116: 106 23 | 12 28
125: 106 12
47: 94 106 | 26 12
67: 4 12 | 78 106
30: 28 106 | 34 12
94: 59 106 | 101 12
61: 100 106 | 27 12
10: 106 4 | 12 4
127: 14 106 | 13 12
77: 106 86 | 12 63
71: 106 124 | 12 48
117: 106 111 | 12 45
15: 43 106 | 23 12
58: 65 106 | 54 12
80: 14 106 | 124 12
73: 52 12 | 113 106
88: 77 12 | 46 106
5: 108 106 | 118 12
89: 5 12 | 122 106
99: 28 106 | 125 12
26: 106 125 | 12 52
113: 12 12
41: 50 12 | 6 106
62: 106 110 | 12 103
48: 12 43 | 106 34
50: 124 106 | 49 12
114: 91 12 | 117 106
121: 87 12
39: 106 87 | 12 23
4: 12 106
103: 106 4 | 12 52
106: "a"
119: 106 64 | 12 93
74: 41 12 | 7 106
31: 12 129 | 106 128
34: 106 106
28: 106 106 | 106 12
49: 78 12 | 28 106
93: 34 12 | 34 106
37: 97 12 | 70 106
92: 75 106 | 16 12
6: 10 12 | 20 106
22: 59 109
7: 66 106 | 123 12
95: 73 12 | 22 106
1: 12 52
23: 12 106 | 106 106
25: 69 106 | 39 12
44: 12 34 | 106 23
57: 99 12 | 54 106
65: 52 12 | 78 106
16: 106 104 | 12 22
36: 12 59 | 106 28
38: 20 12 | 60 106
83: 109 101
29: 12 105 | 106 53
91: 12 96 | 106 76
126: 106 114 | 12 19
81: 108 106 | 116 12
78: 12 12 | 106 106
14: 12 101
84: 44 106 | 104 12
64: 12 34 | 106 68
9: 106 83 | 12 67
111: 106 87 | 12 78
115: 87 109
3: 43 106 | 34 12
108: 43 106 | 28 12
51: 87 12 | 125 106
90: 106 36 | 12 121
2: 21 12 | 29 106
68: 12 106 | 106 12
40: 24 106 | 22 12
85: 12 28 | 106 87
52: 106 109 | 12 106
20: 113 106
76: 12 23 | 106 113
17: 12 92 | 106 55
19: 106 119 | 12 25
8: 42
72: 12 69 | 106 30
43: 109 109
66: 39 12 | 112 106
79: 68 12 | 59 106
96: 109 87

bbbaabaaababbaabbbabbbbbaabbabab
bbbbbbbbbaaaabbaabbaabaa
abaaabaaabaaaaaaaabbaaab
abaaaaababaaaaaababbbabb
bababaaaababbaabbbbbabaa
babaaababaababbbbaabbaabbaaabbbabbabbbaa
aabaaaaabaaababaaaabbbbbaababaaabbabbbba
babbbaaababaaabbaababbabaabbaabb
ababbabbbbabababaaaaababbaabaabb
ababbaabbbbbbabaaaabbbaabababbabbbbbbaaaaaabababbbabbbba
aaabbabababbaababbbabaab
bbaababaaaabbbaaabbabbbbabaaaaaaabaaababbbaaababbabababb
aaaababbbaaaabaabbaaabbabbabbbbbbbabbaaaaabbbaaabbbaabbbbbbaaaba
bbaaabbaabbabbabbbaabbababbbbbaabbbabaaa
aaaaaabbabbabbabbbabbbabaaababab
bababaabbbbabaabbaaaabaabaaaaabaababbbaabbbaaabaabbbbabababaaaaababbbbbb
baababaaababaaababbbabaa
ababbbabbababbabbbabbbaa
babaaaaaabaabbabaaaababbaabbabbbaabbaabbabbabbbbabbbabbbbabbbaab
bbabababbaabbababababaaabbbaaababbbbabaa
bbbaabaabaababaabababbabbaaabbbabbbababaaaabaabbaaaaaabbabbbbaba
abbabbaaabbbbbaaaabaababbabaaabbbaabbaaa
ababbaababbbabbbababbaba
abbaaaabbbbaababbbbbabbbababbaaa
bbabbabaababbbabbbaabaaa
abaababbabbbbbaaababbbba
baabbbaabbababbabaabbbab
bbbaabaaaabbbbaabbbabbbb
abababbaaaabbbbbbbbbaabababababa
aaabaabbababbbaaaaaabaabbabaaabaaaababababaabaabaaaaababbbaaaabbaabbaaab
babaabbababbabaabbabbbaa
baaaabbabaabbbaabbbaaaba
babbaababbaaabaabbbaaabbaaaaabababbababa
ababaaaaaaababbabbbabbaa
bbbbbaababaaaaabbabbabaabaabaabababaaabaabaababbbabbabbb
aaaaaaaabaababbbbaaaaaaa
abaabbabaaababaabbaabbbbaaabbbbbbabaaaaa
baababbbabbaababbbbbaabb
abaaabbaababaaabbbbaababababaaaabbbbaaaa
abbabaaabbabbaaababaabab
babaabbaaaaabaabaaabaabbbaaabaababababbbabbaaaba
abbaaaabbaaababababbbbaabbaaaaababbaaaabbaabaaab
bbaaabbbaabbbaabbaaabbba
bbbaabaaaaaababbbaaabaaa
ababbbabbbabbaabbbaabbaa
bbaababbbaaababbaaabbbaabaabbababaaaabbbbaaabbaabbababaabaabaabb
bbababbbabbbabbabbaabbbbabbabbabbbbabbbaabababbb
baaaaabbaabaaaabbbbbaaab
abbbbaabbbabbbabbaaabaab
baabbaabbbaababaababbabbbabbabbb
bbbbababbbbbbaaaabbbbaabaabaabbaaabbbaaa
aabbbabbbbbaabaaabbbbaabaababbaaabbbaaab
aaabbbbbbabbaabbbbaaaabb
baababbbbabbbaababbaaaba
abbbbbaabbabbabababaaabaaabbaabb
bbbaabbbbaaaaabbbbbaabaabaababbbaabbabab
baabbaaabbbaabbabbbabbab
baabababbabbaabaaaaababbabaababa
babbabaababbbaabababaaba
abbbabbaaaaabbbbaabbaababbaaabaabbaabbbaabaabaaa
ababbbabaababbaababbbaabababbbababaabbabaaaabbba
abbbbaaaabbaabbbbaababbbabbbababbbbbbbaabbabaaabbbbaabaa
bbaaabbabbbabababbbaabba
bbbaaabbbabbaabbbbbaaabb
babbabaaabbabbababbbaaab
bbabbabbbbaaaaabbabaabbaaabbbbab
abababbabbbbabbbbabaabbb
aababbaabbaaabbbaaaaaaba
abbbbabbbabbbaaabaaabbbb
aaabaababbaaabaabaabababaababbbbbbabaaab
aaabbabaaaabbbaababaabaaabbbaabbbbbaaaaa
abbbabbabbbbbaababbabbababbbbabbbaaaaaabbbbabbbbbaabbaaaabbbbbbb
bbbbbaabbbababbabaaaaabbaabaaabb
baaaaaabaabbbaaaaabbbbab
bbaaabbababaabaaabaaabababaaaabb
abbaaaaaaaaaabbbaaaaababaaaabbbaabbababb
babaabababbabbbbabbabbabbabaabbbababbbbaabbbbabbbaaababb
aaabaaaabbaabbbbaabaaaba
bbbbbbbbbabaaaaaabababab
abbbbaaaaaababbaababbbababbaabbbabbaabaa
aabbaabaabaaabbabbabbabbaaabbaabbaaaabab
bbabababababbaabbaaabaaa
aabaababaaaaaabbbababbaa
abaabaabbaabbbaaabaabaabbabbbaaabababbababbbbbbbaabbabbb
aabbabaaabbbbaabbaabbabb
abbaaaaabbababbbabbabbbbbbbaababbabbbbabbaaabbabbbbbaaab
abbaababbabbbbaaaabaabaa
bbaaaaabbaababaabaabababbbbbababbaaabbaa
aaabbbaabbabbaababaaaabb
abbabaaabababaaaaaaaaaba
aaabbabaabbabaabbbbbaaab
abbbbabbbbababbaababaabb
bbbabababaaabababbbbbaabbababaabaaaaaaba
bbababbaaaababaaabbbabab
aabbaabaaaabaaaabaabbabaabaaaabb
abaaabbaabbbbbaabbbbbabb
aabbabaababbabaabbaabbabbaababaabbababbaaabbaabbaabbbbab
bbaabbabbabaaaaababbbabb
aababbbaabaabbabbbabbaabababbaaabbbbbbabbaababbabbaabababbabbbabbbbbaaaa
abaaababbaabababaabaabbabbbbaabababbabbaabaabbba
aaabbaabbabbaaabbababaab
babbbbaaabbbbbabbbbabbba
aaaaababaaaaaabbaaabaabb
babaabaababaaabbabaaaaaaabbaaaabbbababaabaabbbab
aabaaaabaaababbabbbaabbb
aaabbabbabbabbbbaaabaaaabbbabaabbaaabaabbabaaabaabaaabbb
abbabbbbabbabbbbabbaaaabbabbabba
aaabbaabaaababbbababbaaabaabababbababbabaaaabaaaabbbabaa
babbaaabbbaabbbbbabbbbab
bababaaaabbaaabbaaabbbabbabababbaaabababbbbabbbaabaababa
aaababaaabbaabbbabbaabbaabbaaaaabbbababaabbaaabb
baabbabbabaababaabbbabbaabaaabaabaabaabbbaabaaba
aaaababbbbbaabababbbaabaabbabaaababaabaaabbbaaaa
ababaaaababbabaaaaabbbbbaaababaaabababab
abaaababbbbbabbbabbbbabbaaaabaabbaaabaab
aaabbabababbaababaabbbba
bbbbbababaaababaabbaaaababbaabbaaabaaaaababbabba
babaaababbbbbaaabbabbaabbbabbabbbbbaababbabbbababbbbbbbabbbaaababababbaa
abbbbbababbbabbbbbbabababaaababbbbabaaaabaabaaaa
babbaabbbabaaababbbababaabbaaaabbbaabbabaabbabaaaabaaabbaabbaaabbbbaaaba
baaaabbaaabaaaabaaaaabaababaabbabbbbbbab
ababbbabbbabbbbbabbaaaaabbbaaabaabbbbbbb
aababbaabaaaabbabbaabbbbaabaaaabaaabbabaaabaabbaaabababb
aababbaaaaabbbaaaabaaaabbbaababbbbaababaababababbaaabbbbabbbaabb
aabaaaaaaabbbbbbaabaaaaa
ababbbbbaaaaaaababaaaaaabbaaabbbabababaabaabaaaaaabbaabb
bbaaabbbbbbbbbbaaaaabbaa
aaabaababaaababbbbbbbaabaababbaaaabbabbbaabababa
bbabbaaaabaaaabaabbababb
baaaabbbbaaabababaaababbaabbaaabaaabbbba
baaaabbbabbaabbbbbbbbaaabababbbb
bbbbbaaabaabbbaababbbbba
baaaabbaababaaabababbaaa
baababbaabbabaabbbbbaaab
baaaabbabbabbaaaaaabbaababaababbababbbba
abbbabbbabaabaabaaaaaabbbabaabaaababaaabbabbaaaabaaabbbb
abbbbbaaabbabaabaabbbaba
bbbbababbabbaaabbbaababbababaaabbaaababa
baabbaabbbabbbabbbabbbababaaaabababbabab
babaaaaababbaaabbbbbabaa
baababaabbabbababababaaaabaaababaaabbaaa
abbaababaabbaabaaababaaa
bbaaabaaabbbbabbabaaaabaabbbbbaabbaaaaba
babaaaaabbaabbababbbabbbaaababbaaabaaabb
babbbaaaabbabbababbaabbabbabaaba
babbbaabbbaababbbaaabbab
aaabbbbbbbbaaabbabababbaababbababababbaa
ababaaaababbbaabbaabbbbbbaaaabab
baababbaabbbbaaabaaabbbb
aaabaabaaaabbbbbabbabaaaaaabbababaabaabaaaabbabaaabaabaaababaaba
bbabbabbaabbabaabbbbaabb
babbaaabaabbbbaaabbbabbaaaababab
aabbabaabbabbbabbbbabaab
aabaaaaaaabaabaaaababbabbbaaaabbaabaababbbbaaabaabababbb
babaabbabbbababaaaaabbbbbbbabbba
bbbaaabbbbabbbbbbaabaaaa
aaabaabaaabbbbbabbbabbab
abbaabababbaaaaabbbaababbabbbbaabaaabababbbbabbaaaabbbbaababbbbabaaaabab
ababaaaabababbbababaaaab
abbbbbababbaabaaaaabbaaabbbabbbaaaabbbabaabababa
bbbbbaabbbbaababbbbbabaa
ababbbaaabbbaabbbaabbbbbbabbbbbbbaaabbabbabaabbaabaabbaa
baaaabaaabbbbabaababbbaa
bbababbaaaaaababbbaabbabbbaaabbabbbaabba
aaaababbabbbbbababaabbaa
bbbaaaabbbbbabbabbbbbababaaabbaabaabbabb
abbbbabaaaababaaaaaabaab
bbaabbabaabbbaababbabaabaabbbbaababbbaabaaabaabaaaababbb
bbbbbaabaababbaabbbbbaabbbbababb
abaaabbabababbbabbbbaaaaabbaabaabaabbaaaaaabbaba
abbaabbababbaabaabaaabbb
aaabbabbabbabaabaaababbb
bbbbababaababbaabbbbaaab
baababaaaaaaaaabbabaaabababbbaabbabbbaba
aaabbababaaababbbbbbababbabaabaabaababaababaaaab
baaaaaababbbabaabaaaaaaaababaabaaabaabaaabbababa
bababbabbbabbabaabbbbaabaabbabab
aaaaabbbaabbbbbaabbbaaab
baaababbaaaaaabbaaaabbbbbbaaabbababbbabb
baaaaabbaaaaaaaaaababaaa
aaabaaaaaabbbabbbababbabaabbbabbaabbabbbbbabaaab
babaaabaaaabbabbaaabbaababababbbbbaabbaa
babbbabaaabbbababaaaaaaa
abbbbaabaababbaaabbbbbaaababbbbbbbbaaaba
aabaaaabaabaababaabbbabbbababaaaaaabbaaa
bbabbbbbabbaaaaabbaaabbabbabaabb
abbabaaababbbaabbbabbbba
abababbaabbbabbbbbabbababaaaabbbbaaabbab
bbabbbababbaaaabbbababbbbaaababbbbabbbaa
bbaabbbbaaabaaaabbababbabbbbbbbbaaaababa
bbabababbbaaabbbababaaabaaaaabbbaaaaaabbabbbbbabaaabaaabbaaabbba
abbbaabababaaaaaaaababaaaaaabbbbbbabbbbbabbbbbbbbaabbaaaaabbbbab
bbbaaaabaaaaabbbbbbbaaab
bababbabbbaaabaaabaababbbaababbabaaaabaabbbbaabb
aaaabbbbbaaaaaabababbbba
aababbaaabbaababababbbabaababbaaabbbaabbaabbabbb
baaaababbbabbaaaaababaab
babbbaaabbaababbabbababa
aabbaaaaababaababbaaaabb
babbabaabbabbabaabbbbaaababbaaaa
abaaaabaabbaaaaaaabbabab
bbaabbbbaaababbaabbabbbbaabbbaabbaaaaaabbabababa
bbaaaaaaabaababbbabababa
baaaabbbaaabbbbbbbabbbba
bbaaaaabaababbaabbbbbbbbbabbaababbbbbbba
baabbbaabbaaaaabaabaababbabaaaaaaaaabbabbbbbabaa
babaabaaabbbbbbbaaaaabbabbbbaaaababaabaabbbbbbabaaaabbaabbbbbbaabaabaaab
babbbaabbbbaabaaaaababaaaaabbaabbbabaaba
bbababbbaaabbbbbbbaaaabb
ababbbbbaaababaaaabbbaaa
ababbaabbbabbbbbaaabaaab
abbabaaaaaabbabbabbaababaabbabba
abbaaaaabbaabbbbaaaaababbbbbbaabbbbabbbaaaabbbab
baaaaabbabbbabbbabbbbaabbabbabaabbaaaaababbaaabbabbbbbbb
bbaaabbbbaaaaababbbaabba
aaabaaaaaabbbbbabaabbbaabaabaababaabaabb
aabaababbaaaabaaaaabaaaababaaabbbabbabab
aaabbaababbbbbababbabbbbbbbbabaa
bbababbbbaababbababbbaaabaabbabb
bbaabbbbbabbaabbbaaabbab
abbbbabbaaabbbaaaaaaabaaabbbabbbabbaababbababbaaaababbbaabaaaabb
abbbbabaaabbabaaaaabaabaabbbbabbbabababababbabba
abbbabbbababaaaaaabababb
baaaaaabbabbabaaabababab
aabbbaababbbbaabaabbabba
aabaaaababaaababbbababaa
ababbbbbaababbabbbaaabab
abbabbaaababbaababbbaaab
aaaabaabaabaabbbbbbabbaa
bbaabbabbaabbbbbababbbba
aaaaabbbaaaaaabbbbaaabbabbbaabaaaabbabbb
abbabbabababbabbbaabbbab
bbaaabbbaaaaabbbaabbabaaaabaabbb
baababbabaaabbbabbbabbba
aabaaabbbbabaaabbaabbabbbbaaababaabababb
bbaaaaaaababbabbbbbabbba
bbaababaabbbbaabbbbabbab
bbabababbbabbaaababbbbaaabaabbabaababbaabbbbaabbbbabaaaa
abbbbbaabbbbbabaaabbabbabaabbbbabbabaaaababaaabbbbaabbabbbbbbabbbbbaabbb
aaababaababbaabaabbaababbaaaaababbabaabaaabababb
bbaaabaaaaaabbbbbbbbaaaaabbbbbaabbbbabbabbabaaabbaaabbaababbbbbb
abbbaababbbaababbabababa
aaaaaaabbaaaabbababbbaaababaaabbabbbabaabbbaabbaababbbba
bbbbaaaaabbbbababababbabbabbabbb
abaababbabbabaaabbbbaaab
baaaaaabbabbabaababbaababababbbb
bbbaaaabababaaaaaabbabab
aaabbaabbaaaaababbaaabbaabaababbaaaaaaabbaaaabbbbbaabbba
baabababaababbabaabbbbab
abbbaababbbaaaabaaabbbbbaaaabbaababababbbbaaaababbbbbabb
aabaabbabaaababbbabbabab
aaababbaaaabbaabaabaabbb
aaababbaaaaaabaaabbaaaaabbbabbab
abbbbbababaabaabbababbbb
aaaabbbbbbababbabbaaabaaaabbbaaa
bbabbaababbaaaaabbabbbbbabbaaabaaaaaaaba
bbababbaaaaaababaaabbbbbbbabbbabbbaabaaa
abababbaaabbbaabbabbbaaabbaabababbaababb
bbabaabaaaabababbbbaabaaabbbabbbbbaabbaaabbbbabaabbbbaaa
baaaaabbbaaaabbabbbbabababaabaabababbabaaaabbbba
bbbbababbbabbaaaaaaabbbbbaababbabaaabbba
ababbabbbabaaaaaabaaaaaabbbbbbba
aaaaabababaaaaaaabbbbabbabaaabaabaaaaaba
aabbbaababbabaababbbabaa
abaabbabaabbaabababaabaabbbbabababbababbabaabbaa
bbbbbbbbbabaabaaaaabaababaababbbababaaaabbbbbbbaabbaaabaaababbbbbabaabbb
abbabbbbabbbabbaaaabaaab
bbbbbbaabaabababbaaaabbbbaaabbaa
ababbbababbbbbaabbaababababbbbba
bababbbabaabbaabbbbbaaab
baabbaabaaaaabaaabababab
abbabbbbaaabbabbaaabbaabbbbbbbbbbaabaabababbabaabbbbaaab
babbaaabbbabbbbbbbbbbbbbaababaab
babbbbaababaaabaababbbba
aaaaabaaabbbbaaabbabbbabaababbbbbaaabaaa
abababbabaabaabaabbabbba
aaaaaabbaababbaaaaaaababbbaabbabaaabbbbaabaaabbbbbbaaaba
ababbbbbabbabbbbabaabbabbabaaabbabaabbabaaababbb
bbaaaaabaabaababaaabaabaabbbbabbbaabbaaa
baaabababbaaabbaaabbbbab
baaaabaabaaaabaaaaaaabababababbabbbbaabaaaabbaabaabaabbbbaabbaaa
aababbabaabbbabbbbbabaab
baabbaabbaaaaabaabaababa
baaababbaaabbabbabbbaabb
baabbbaabbbbaaaaaaabaaab
bbabababbabbbaaaaabaaaba
abbabaababbaabbbaabbaaab
babbaabbaaabbababbababaa
bbabbababbababbbaaabaabb
bababbbaaaabaababaaaabbaabaabbbb
bbbbababbabaaabaabbbbaaabbbaabaaababaaaaabbaaabbbabbbbabaaaababa
ababbaabababbbababbabbbbbbaaabaabbabbbba
aaabaabaaabbaababbbbabbabbbbbbab
babaaaaaababbabbbbbbaaab
bbbbbababbaabbabbaaabaaa
bbababbaabbbbbaabbabbaababbaaaaabbbabaaa
bbabbababbababbbbabbbabb
aaaaababbbbaaabbbababbbaaaabbbaabbbbabbbaaaababaabbbbbbbaaaabaababbbabaa
bbbbaabaababaaabbaaaaaaa
abbabaaaabbbbbaabaabaaab
bbbaaaabbaaababbbaaaaaaa
babbabaabababbabbbaababbabbbaaab
abababbababaaabbaabaabaa
bbabbababbbbbbbbabbaabaa
bbbbaababbbbabbbabbbbbba
aaabbabaabaaabbaababbabbababbbbbaababbba
bbaababbabbbbaabaaabbabbabbaaaaabbaabbbaabbbbbbb
aaaababbbbbbbabaaaababaaabbabbbbabaabaaa
bbababbbababaaabaabbabab
aabaaaabaabbabaabaaabaab
bbaaaaaaaaaababbabaaaabb
aaabbabbbbbbaabaabaabbbb
aaaaabbbabbbbbabaabaaaba
abbbabbbbbbababababbbaaaabbabbbbbabaabbb
abbaaaabbbabbabaababbaaa
abbaababaaabbbbbbabaaabaabbbbbaaabbbaaaaaabababbbababbbbaaaabbabaabaabaa
bbabbababbaabbababbabbabbbbbababaabbbaba
bbabbbababbaaaabaabaababbabababbababbbba
ababbbbbbbabbabbbabbabba
aaabaaababbaababaabaaaaabababaaabaabaabaaababaaaaababbbaabbabaabbbbbabaabaabbbabbababaababaabbaa
aaaaababbabbabaabbbbbabb
aababbaababaaabaaabbabab
bbaaaaabbbababababaababa
aabaaaabaaababaabbaabbba
ababbbbbabaabaabbaabbaabbabbbbab
abbbbabbababbabbabaaaabaaabaabaabaaabbba
abbaaaababbbbaaaabbaabbbaabaaaba
abbbabbabbbbbaabbbabbbbbaaaababa
ababbabbbaaaaabaababaaba
abbaaaaabbbbaabaaabaabaa
bbbaaabbbabbbbaaabbaaaaabaaabbbb
aaaaabababbaabababbababa
aabaababbababbbabbabaabbbbbbbababababaababbaabaaaaaabbbababbabaaaabbabbaaababbabbabbbaaabababaab
aaaaababbbbbabbbbbaabbbbbbaaaababaaaabab
bbaabababbaaaaaababbabbb
bbbaaabbabbbbaaabaaabbba
bbbbbaaabaabbabaabbbbaaaabaabbaabbaaaabb
abbbbbabbaaaabbbbabaaabbaaaaaabbabaaaaababbaaabb
bababbabaababbaaabaababbabaabaaa
bbbbabbbbbaababbbbaaaaabbabbaabbbbababbbaaabaaaaaabbabbb
bababbabababbbabbabbaaabbbaaabbbababaaaabababbabbbabaabb
abaabbabbbbbbaabbaaaabbbabbbbaabbabaaabbbaabbabbbabbbbbbbaaabaaa
baaabababbbaaaabbababbabbabbabaaabbbaaab
bbbaabaabbabbabbaabaaaaa
abaabbabbbababbaaaaabbaa
aabbbbbaabbbabbbaaabaabb
babaaababaabababaabbabba
bbbbabbbbaabbabaaaabbaabbbbaaaabbaaaaaabbaabbaaaaaabbaaabbbbaabbbaaaabab
bbaababaabbbabbbbaaabaab
abaababbbabbaabbbabababa
ababbbababaaaaabbbabaaaa
bbbbbbbbabbbbaababbabbaaaabbbbbabababbbaabbbaaaa
abbabbbbbabbbaaabbbbbbbbaabaabaa
abbabbbbaabbaababaabbababbaababbbaabababaabbbabaaaaabbaa
bbabbbbbbabbbbaabaabbabb
abaaaabaaabbaabaabababaa
aaaaabbbbaaababbbbaabaaa
abbabaaabbaaabbbbababaab
ababbabbbbabababbaabbbba
aaababaabbabbababbbabbaa
bbbbaabaaaabbababbbabbbb
babbaaabbbbbababaaaababa
baababbabaaaabbaabbbbabaaabaabbb
bababbaaabbbbabbbbbaaaaabababaaabbabbaaababbbbbbaababbaabbbbabaaabaabaaabbaaabbaabaababa
bbabbabaaabaabbaaabbbbab
aabbaabaabbabaaaaaaabbaaabbbabaaabbbaaab
abaabbabababaaaababababa
baaaaaaaabaaabbbabbbbaaabbbabaabaaaabaaa
aabaababbbbbbbaaaaaabbab
abbbbbabaaaaaaaabaaabababbbabbbaabbbaaaa
bbbbbaababbbbabbaabbabba
abbabaababaabaabaababaaa
aaababaaabbbaababbabababbbbbaaababaabaaa
aaaaaaaaaabbabaaaababaaa
aaabbabbbabaaabbbbababaa
baaaaabbbbbbbbbbababbbbbaabbaaab
baaaaaabaabbabaabbbbbaabbbababbbbbbbaaab
bbbbbbabaaaaabbbabbaabbbbbabbbbbbabbbbbababbbaabbbbabbaa
babbaabaaaaabaabbabaabbbbbbaaaaaaaababab
bbaababbabbaababbbabbabaababbaaabbbabbaa
aaababaaababbaabaaaaabba
bbbbbbbbaaaababbbbaabaaa
bbababbabbbbbbaaaabaabbb
bbbaaabbaaabbaabbaaaaaaa
aaababbaaaabbababbabbbbbbaabbaabbbbbaaab
babbaababaababbbbbbbaaaabbaaabaabbaabbba
bbbaababbaaaabbbbababaab
bbaababbbbaabbbbbbaabbaa
babaaaaaabbabaaaabbabaabbbbbbabbaabbbbab
baabbbbbabbbbabaaaababbb
baabbabaabbaabbbbabbabbb
abbaabbbaaababbaabbbbbabbbaabbababababbabbbbbbabbabaababaabbbbbb
aaaabbbbaabbbaabbaaaaabbabbbbaaababaaaaaabbbaabb
baababbbbbaababaabbabbaabbbbababbabbaabaaaaababbbaabbbbaabababaa
baabababaabbbbaabbabbbaa
aaaaaaabbaaababbaaaabaab
aabaababaaabaaaabbbbbbaaaaaabaaa
baabbaabaaaababbbbaaaabb
abbabbbbaaabbaababbbabab
aaabbababbabababaabbabab
babaabaaaaaaabaabbaababbaabbbbbaaabbbbaaabbababbbabaabbbbbabaabbbbababaa
bbbbabbbaabbbbbabaabaabb
aaabbbaaaaabbabababbbaabbababaaaabaabbaa
baaaaababababbbabaabaababaaabbab
aaaaaaababbbabbababaaabbaaaababaabbbbbba
abbbaabaabaaabbaaabbaabb
aabbaabababaabaabbaabbaa
bbababbbabababbabbaabbaa
bbbbbababbabbaababbbbabaaaaaabbbaabababaaaabaaab
baaababbababbaabbbaabaab
baabaababaabbabaaabbaaaaabaaaabb
abbabbbbababbaabbbababaa
bbbbaabababaaabbaababbaababbaaabbbaaabab
aabaababbaababaabaaaabbbabbaaabb
babbbaaababbaaabbababbbababbbbab
bbabbbababaaabaaababbabbbbaaaaaababbbbbb
aaaaaaababbabbbbabaaababbaabababbbbaaaba
abababbabaababaabbababaa
baaaabbbbbabbaabbabaaabababaaabbabaababbabaabbba
bbbbabbbbbaabbbbbbaaaabb
bbababbbabaabaababbaaabb
bbaaabaababaaabababbabab
baaaaabbaaaababbaababbbb
aaaabbbbabbbbaaababbbbbb
abbbbbaaabbabbaabbbbbaaaababbbbaaababbba
abbbbaaababaabaaabaabbbb
abaabaabbaabbaabaaabbabaaabbabba
ababaaababbbbabbaaababaabaabbbaaaabbaaaa
babbbbaaabaaababababbbabaaaaabba
bbabbbababbaabbbaaaabbbbabbaaaaaabaabbaababbbbbb
aabbaabbbaababbaabbabbbbabaabaaaabbaaababaaaabbb
bbbbbbaaabaaaaaaaaaaabba
abaaabaaabbaabbbababaaaaaabbbbab
bbaaabbbbaabababbbbababababaabaaabaaaababbaaabba
baababaabbbaaabbaaabbabbaaaaaaaaaaabaaaaaabbabab
bbaabbbbbabbabaabaabaabb
bbbaababaaaaaaaababbbaabaababbbbbaaaabab
baabbabaabbbabbabaabaabaababbbabbaabbbaabbababbbbabbbababbbbbabbbbabaaaa
baabbbbbabbaababbbbaaaabaababbaabbbbabbbabaaabaaaaabababbabbbbabababaabbbaabaaab
abaaabababbbbababaabbbaaaababaaaaabaabaa
bababababbbabbaaabbaaabb
baaaaabbabbbbaabaabaaaba
aaaaababbbaabbbbbababaaaaaababbabbaaaabbbbbabbaa
bababaaaaaaaababababbbba
bbaaabbaaaaaaaaaaababaaa
babbaabbabbbabbbbbbbabbbabbabbbb
babbbaaaaaaaaaaabbaabaab
abbabbaabbabbababbbbaaaaabbaaaba
abbabbababbaaaaabbaaabbaabbaabbabbbbaaab
aaababbababaaabbbaaaabab
aaaaaaabababbabbabbaabbbaabbbbbb
abbbaabaababaaaaaaaabbaa
abaaabbabbbbaaaabbbababb
bbbbbaababbbbabbbabaaaaabbbbbbaaabbabaababaabaaabbaaaababaabbbba
baabbbbbabbbbaaabbabbbabbaabababbbbbbabbbabbabba
aaaaabbbbabbabaaaaababbb
babbbbaabbbbbaabbbabbbbbabbbbbaabbbbbbaaaabbaaaa
abbabaaaaaababaabbabbbabaabbbbbaabbbabbbbabbbbba
abbaabbbbbabbaaaaabbbabbaabbabaaaababbbaaababaab"""
    main(myInput)
