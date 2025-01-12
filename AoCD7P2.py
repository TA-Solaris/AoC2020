### Advent of Code - Day 7 - Part 2 ###

### Defining Classes
class Graph():
    def __init__(self, myInput):
        ### Defining Properties
        self.nodes = []
        self.edges = []

        ### Handling Input and Building
        myInput = myInput.replace(" bags", "")
        myInput = myInput.replace(" bag", "")
        myInput = myInput.replace(".", "")
        myInput = myInput.splitlines()
        self.build(myInput)
    
    def __repr__(self):
        return f"{self.nodes} {self.edges}"
    
    def build(self, myInput):
        for rule in myInput:
            key, value = rule.split(" contain ")
            parts = value.split(", ")
            keyNode = self.getNode(key)
            for part in parts:
                if part != "no other":
                    weighting, partNode = part[0], part[2:]
                    weighting, partNode = int(weighting), self.getNode(partNode)
                    self.edges.append(Edge(keyNode, partNode, weighting))
    
    def checkNodeExists(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    def getNode(self, name):
        node = self.checkNodeExists(name)
        if node == None:
            node = Node(name)
            self.nodes.append(node)
        return node
    
    def getEdges(self, node):
        edges = set()
        for edge in self.edges:
            if edge.fro == node:
                edges.add(edge)
        return edges
    
    def getBackwardsEdges(self, node):
        edges = set()
        for edge in self.edges:
            if edge.to == node:
                edges.add(edge)
        return edges
    
    def getBFS(self, start):
        visited = set()
        queue = [self.getNode(start)]
        while queue:
            for e in self.getEdges(queue[0]):
                v = e.to
                if v not in visited:
                    queue.append(v)
            visited.add(queue.pop(0))
        return visited

    def getBackwardsBFS(self, start):
        visited = set()
        queue = [self.getNode(start)]
        while queue:
            for e in self.getBackwardsEdges(queue[0]):
                v = e.fro
                if v not in visited:
                    queue.append(v)
            visited.add(queue.pop(0))
        return visited
    
    def getSubBags(self, start):
        total = 0
        for e in self.getEdges(start):
            total += e.weight
            for _ in range(e.weight):
                total += self.getSubBags(e.to)
        return total

class Node():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class Edge():
    def __init__(self, fro, to, weight):
        self.fro = fro
        self.to = to
        self.weight = weight
    
    def __repr__(self):
        return f"{self.fro} {self.to} {self.weight}"

### Defining Subroutines
def main(myInput):
    myGraph = Graph(myInput)
    print(myGraph.getSubBags(myGraph.getNode("shiny gold")))

### Name Guard
if __name__ == "__main__":
    myInput = """striped green bags contain 5 posh indigo bags.
light yellow bags contain 3 wavy turquoise bags.
bright lime bags contain 2 striped crimson bags, 3 dull red bags.
dull blue bags contain 4 posh coral bags, 3 mirrored coral bags, 2 striped fuchsia bags.
vibrant coral bags contain 2 shiny blue bags, 2 muted gray bags.
mirrored gold bags contain 2 dotted maroon bags.
drab lavender bags contain 4 pale turquoise bags, 5 faded lime bags, 2 bright aqua bags.
mirrored red bags contain 4 shiny tan bags, 4 muted aqua bags, 4 pale salmon bags, 5 bright violet bags.
clear gray bags contain 4 bright lavender bags, 2 dotted plum bags, 1 drab coral bag, 3 faded aqua bags.
dull aqua bags contain 2 wavy coral bags.
muted yellow bags contain 3 drab olive bags, 4 pale lime bags, 2 striped crimson bags, 3 wavy blue bags.
shiny chartreuse bags contain 5 bright yellow bags.
posh turquoise bags contain 3 dotted blue bags, 4 pale lime bags, 1 mirrored fuchsia bag.
faded maroon bags contain 5 striped indigo bags, 2 light aqua bags, 3 dim chartreuse bags, 4 vibrant tomato bags.
dotted lavender bags contain 3 pale crimson bags, 3 wavy gray bags, 2 plaid plum bags, 5 mirrored bronze bags.
striped olive bags contain 5 dull lime bags.
vibrant aqua bags contain 3 drab tan bags, 5 bright coral bags, 3 pale brown bags.
wavy aqua bags contain 4 dim lime bags, 4 dotted bronze bags, 1 bright gray bag.
pale green bags contain 1 shiny purple bag, 4 dim plum bags.
vibrant purple bags contain 2 pale gray bags, 2 dull crimson bags.
faded green bags contain 4 dotted plum bags, 1 light white bag.
posh orange bags contain 4 light blue bags.
drab tomato bags contain 1 dull salmon bag, 3 plaid orange bags, 3 posh gray bags.
vibrant beige bags contain 2 dull fuchsia bags.
wavy orange bags contain 2 bright tan bags, 5 light beige bags, 2 vibrant turquoise bags.
light salmon bags contain 1 dark blue bag, 2 bright orange bags.
light blue bags contain 3 clear chartreuse bags, 5 dull olive bags.
dull crimson bags contain 4 dim gold bags, 5 dark tan bags, 5 dark lavender bags.
dim teal bags contain 3 striped gray bags, 4 shiny fuchsia bags, 2 vibrant chartreuse bags, 2 drab plum bags.
striped crimson bags contain no other bags.
dark brown bags contain 1 dim plum bag.
dotted tan bags contain 1 striped fuchsia bag.
bright turquoise bags contain 3 light orange bags, 2 wavy bronze bags, 2 light beige bags.
drab salmon bags contain 4 wavy silver bags.
light brown bags contain 1 clear gold bag.
plaid aqua bags contain 4 shiny maroon bags, 2 mirrored gray bags.
posh chartreuse bags contain 3 clear maroon bags, 4 wavy black bags, 3 vibrant white bags.
wavy gray bags contain 3 shiny violet bags, 2 striped silver bags, 5 pale lime bags.
dim crimson bags contain 1 wavy blue bag, 1 dull red bag, 1 dotted plum bag.
wavy black bags contain 5 dim crimson bags, 5 dotted chartreuse bags.
faded gray bags contain 4 plaid white bags, 2 mirrored yellow bags.
muted violet bags contain 5 vibrant blue bags, 5 shiny beige bags.
dull white bags contain 1 dull olive bag, 5 clear chartreuse bags, 1 dull red bag, 1 wavy red bag.
light bronze bags contain 4 bright gray bags, 3 light tomato bags, 2 shiny white bags, 2 clear silver bags.
plaid violet bags contain 2 vibrant indigo bags, 2 dim turquoise bags.
posh purple bags contain 5 wavy purple bags.
bright olive bags contain 4 muted bronze bags, 4 mirrored green bags, 2 dim plum bags, 5 bright silver bags.
vibrant olive bags contain 1 vibrant beige bag, 4 striped gold bags, 4 shiny beige bags, 1 faded blue bag.
muted fuchsia bags contain 3 vibrant red bags.
plaid indigo bags contain 4 dull lime bags, 3 faded violet bags.
wavy chartreuse bags contain 3 dotted yellow bags.
posh magenta bags contain 4 bright gray bags, 4 dotted turquoise bags.
drab teal bags contain 5 dotted plum bags, 2 light white bags, 2 dark plum bags, 4 dim crimson bags.
dark coral bags contain 3 wavy chartreuse bags, 3 plaid bronze bags, 1 muted magenta bag.
posh white bags contain 4 dotted turquoise bags, 1 mirrored lime bag.
mirrored brown bags contain 2 shiny chartreuse bags, 1 light bronze bag, 4 bright bronze bags, 5 dotted crimson bags.
faded cyan bags contain 2 dull crimson bags, 4 light chartreuse bags, 4 light salmon bags.
bright maroon bags contain 3 dotted yellow bags, 1 bright gray bag, 2 dim yellow bags, 5 light fuchsia bags.
clear silver bags contain 4 faded green bags, 4 posh white bags, 4 dark plum bags.
shiny crimson bags contain 4 dark lavender bags, 3 dotted gold bags, 3 dark tan bags.
wavy olive bags contain 4 dotted cyan bags.
wavy coral bags contain 3 dim gold bags, 4 dim silver bags, 4 faded green bags, 2 muted purple bags.
striped chartreuse bags contain 4 mirrored plum bags, 4 dull tan bags, 5 muted gold bags.
bright blue bags contain 5 mirrored beige bags, 4 muted bronze bags, 1 dark tan bag, 5 dark cyan bags.
vibrant red bags contain 3 light chartreuse bags, 2 faded indigo bags, 3 drab teal bags, 1 striped indigo bag.
dim cyan bags contain 5 faded silver bags, 3 wavy coral bags.
muted gold bags contain 4 pale coral bags.
wavy violet bags contain 2 dotted gray bags, 1 clear tan bag, 5 plaid brown bags.
light maroon bags contain 5 faded silver bags.
light cyan bags contain 5 pale brown bags, 3 pale black bags, 3 light tomato bags, 2 faded violet bags.
pale turquoise bags contain 1 dull white bag, 1 muted tomato bag, 2 clear gold bags.
clear plum bags contain 2 dotted orange bags, 1 bright olive bag, 3 striped violet bags.
plaid silver bags contain 5 muted olive bags, 1 vibrant bronze bag, 5 dull lavender bags, 3 dark purple bags.
clear gold bags contain 1 dotted turquoise bag, 3 dark indigo bags.
muted indigo bags contain 1 mirrored orange bag, 3 dull beige bags.
light plum bags contain 3 drab brown bags, 4 wavy cyan bags, 3 vibrant lavender bags.
dim maroon bags contain 4 dull tan bags.
pale lime bags contain 4 dotted maroon bags, 2 faded silver bags, 5 shiny tomato bags.
shiny black bags contain 2 dull crimson bags.
wavy indigo bags contain 1 light fuchsia bag.
dull lime bags contain no other bags.
shiny fuchsia bags contain 2 drab fuchsia bags, 1 shiny cyan bag, 1 muted black bag, 2 dull aqua bags.
muted lavender bags contain 4 dull fuchsia bags, 1 dim chartreuse bag, 1 vibrant gold bag, 2 shiny beige bags.
bright cyan bags contain 5 dark gold bags, 2 vibrant cyan bags, 1 pale coral bag.
posh black bags contain 3 dull violet bags, 5 drab coral bags.
posh olive bags contain 3 muted magenta bags, 3 dark plum bags, 1 shiny violet bag.
dull coral bags contain 1 dark gold bag, 2 striped silver bags, 5 vibrant lavender bags, 2 light red bags.
clear bronze bags contain 4 striped cyan bags, 4 dotted chartreuse bags, 4 shiny maroon bags.
bright red bags contain 2 dark violet bags, 4 pale brown bags.
muted silver bags contain 3 bright blue bags, 1 shiny blue bag, 5 muted bronze bags, 1 bright tan bag.
dotted maroon bags contain 5 muted white bags, 4 dull lime bags, 2 dim gold bags, 2 faded fuchsia bags.
clear lime bags contain 4 striped gold bags, 2 vibrant purple bags, 5 dotted green bags, 2 light tomato bags.
shiny tan bags contain 5 dark lavender bags, 1 dull red bag, 4 vibrant turquoise bags, 5 faded fuchsia bags.
dark teal bags contain 2 dotted brown bags, 5 clear salmon bags, 5 wavy coral bags, 3 light fuchsia bags.
shiny cyan bags contain 1 mirrored gold bag, 1 mirrored aqua bag, 1 posh magenta bag.
pale red bags contain 1 vibrant turquoise bag.
drab coral bags contain 2 faded tomato bags, 3 plaid aqua bags.
clear white bags contain 1 dull white bag, 5 shiny tan bags, 1 mirrored yellow bag, 1 wavy chartreuse bag.
clear crimson bags contain 5 muted white bags, 1 vibrant yellow bag.
posh lavender bags contain 2 mirrored aqua bags, 4 faded aqua bags, 2 light red bags.
dim violet bags contain 4 dull orange bags, 5 dull turquoise bags, 5 dark purple bags.
pale beige bags contain 3 wavy indigo bags, 5 dark plum bags, 2 dark purple bags, 2 dim turquoise bags.
striped brown bags contain 4 bright lime bags, 5 wavy coral bags.
shiny blue bags contain 2 wavy coral bags, 2 dotted plum bags.
pale black bags contain 5 clear maroon bags, 4 striped crimson bags, 4 dark gold bags.
drab plum bags contain 3 clear gold bags.
posh beige bags contain 3 faded silver bags, 3 dim gold bags, 5 shiny gold bags.
clear lavender bags contain 1 clear white bag.
light lavender bags contain 4 dotted violet bags, 3 dull violet bags, 4 dark maroon bags, 2 striped violet bags.
plaid brown bags contain 4 dotted yellow bags.
dotted green bags contain 3 dull red bags, 2 faded green bags, 3 muted white bags, 1 dim turquoise bag.
muted olive bags contain 4 vibrant tan bags, 3 dotted black bags.
light turquoise bags contain 3 wavy blue bags, 4 dim plum bags, 4 dim chartreuse bags.
dim salmon bags contain 2 mirrored yellow bags.
shiny white bags contain 1 mirrored violet bag.
drab olive bags contain 3 striped crimson bags, 3 dotted maroon bags.
drab silver bags contain 5 shiny cyan bags, 1 dull teal bag, 4 dark lime bags.
vibrant turquoise bags contain 4 striped crimson bags, 5 dark plum bags, 3 dark lavender bags, 5 dark purple bags.
shiny purple bags contain 1 posh beige bag, 1 dark indigo bag, 4 plaid fuchsia bags, 5 dotted green bags.
bright brown bags contain 1 striped lavender bag, 5 light gold bags, 1 dim maroon bag.
dotted violet bags contain 3 striped blue bags.
bright crimson bags contain 2 muted gold bags, 3 vibrant turquoise bags, 3 wavy green bags, 5 dull white bags.
striped tan bags contain 2 wavy gray bags, 4 bright gray bags, 1 plaid cyan bag, 1 vibrant magenta bag.
dull green bags contain 1 bright brown bag, 5 posh beige bags, 5 mirrored crimson bags, 1 dark silver bag.
mirrored lime bags contain 4 muted tomato bags, 5 wavy chartreuse bags, 5 dotted plum bags.
striped beige bags contain 2 striped bronze bags, 2 shiny yellow bags, 4 pale gray bags, 2 vibrant tomato bags.
vibrant lime bags contain 4 striped crimson bags, 2 pale silver bags, 4 clear purple bags.
pale blue bags contain 1 bright cyan bag, 1 shiny fuchsia bag, 5 wavy turquoise bags, 5 dotted silver bags.
striped maroon bags contain 1 muted lime bag.
faded chartreuse bags contain 2 mirrored white bags.
mirrored crimson bags contain 2 dotted gold bags, 5 shiny red bags, 5 wavy red bags.
dull beige bags contain 2 posh red bags, 1 vibrant turquoise bag, 5 dark plum bags, 5 clear aqua bags.
wavy green bags contain 3 shiny crimson bags.
striped salmon bags contain 2 dim plum bags, 2 mirrored indigo bags.
faded coral bags contain 3 muted tomato bags, 1 light chartreuse bag.
dark blue bags contain 2 shiny violet bags.
shiny gold bags contain 1 dull lime bag, 2 pale coral bags, 1 wavy silver bag, 5 muted black bags.
clear turquoise bags contain 1 posh magenta bag.
dotted salmon bags contain 2 mirrored lime bags, 1 mirrored salmon bag.
pale gray bags contain 3 bright blue bags, 5 muted tan bags.
shiny teal bags contain 5 pale indigo bags.
drab beige bags contain 5 faded indigo bags, 5 vibrant bronze bags, 4 pale lime bags, 3 dark black bags.
vibrant white bags contain 5 striped violet bags, 3 bright blue bags, 2 dim gold bags.
posh aqua bags contain 5 plaid violet bags, 3 drab chartreuse bags.
plaid gray bags contain 5 dotted cyan bags, 2 mirrored silver bags.
clear indigo bags contain 1 bright tan bag, 2 dull yellow bags, 5 mirrored lavender bags, 2 mirrored fuchsia bags.
mirrored turquoise bags contain 3 faded chartreuse bags, 2 drab turquoise bags.
dark chartreuse bags contain 2 mirrored silver bags, 3 vibrant crimson bags, 4 shiny green bags, 1 pale brown bag.
pale tomato bags contain 2 light gold bags.
mirrored purple bags contain 1 light magenta bag, 3 shiny yellow bags, 4 striped lavender bags.
mirrored blue bags contain 3 posh magenta bags, 4 dark lavender bags, 5 striped crimson bags.
dull purple bags contain 4 mirrored indigo bags, 2 wavy bronze bags, 4 muted white bags, 4 shiny crimson bags.
mirrored teal bags contain 5 dim teal bags, 4 dark lime bags, 4 mirrored yellow bags, 3 mirrored turquoise bags.
drab gold bags contain 3 dark maroon bags, 2 plaid beige bags.
dotted gold bags contain 2 striped crimson bags, 3 clear red bags.
posh fuchsia bags contain 4 dim cyan bags, 4 vibrant turquoise bags, 4 dotted plum bags.
dim lime bags contain 4 posh indigo bags.
dim tan bags contain 3 pale indigo bags, 1 striped turquoise bag, 4 plaid coral bags.
plaid red bags contain 5 wavy gold bags, 1 muted plum bag, 2 vibrant plum bags, 1 dim brown bag.
light orange bags contain 4 dotted teal bags, 4 dotted yellow bags.
dark green bags contain 1 dull cyan bag.
posh coral bags contain 3 shiny green bags, 3 dotted red bags, 1 drab silver bag.
striped orange bags contain 3 plaid plum bags.
pale purple bags contain 1 vibrant coral bag, 2 shiny olive bags, 1 clear orange bag.
bright fuchsia bags contain 3 bright yellow bags.
striped red bags contain 2 bright orange bags, 3 mirrored yellow bags, 1 dotted coral bag, 3 clear aqua bags.
faded plum bags contain 2 shiny tan bags, 4 dull tan bags.
striped gold bags contain 1 shiny crimson bag.
faded olive bags contain 2 shiny lavender bags, 5 posh fuchsia bags, 3 pale gray bags.
pale aqua bags contain 3 posh beige bags.
dotted plum bags contain 4 clear red bags.
dotted chartreuse bags contain 1 light white bag, 5 drab turquoise bags.
striped tomato bags contain 4 dim plum bags, 1 striped black bag, 4 drab black bags.
shiny lime bags contain 3 drab coral bags, 1 drab green bag, 4 muted salmon bags.
dim orange bags contain 2 striped chartreuse bags.
plaid tan bags contain 5 light chartreuse bags, 1 dotted maroon bag, 2 clear silver bags.
dull olive bags contain 3 muted gold bags, 5 dotted gold bags, 4 muted white bags, 1 shiny violet bag.
dotted beige bags contain 1 clear tan bag.
dotted silver bags contain 2 faded crimson bags.
muted black bags contain 3 clear red bags, 3 dotted maroon bags.
clear purple bags contain 5 dotted plum bags.
striped indigo bags contain 5 mirrored blue bags, 2 striped violet bags, 3 striped yellow bags.
faded teal bags contain 2 light black bags, 1 vibrant maroon bag.
drab red bags contain 3 dark tan bags, 4 pale red bags, 5 faded salmon bags, 3 dotted tomato bags.
muted aqua bags contain 2 striped purple bags, 3 vibrant orange bags, 3 bright cyan bags.
mirrored black bags contain 4 muted yellow bags, 5 light fuchsia bags.
dark gold bags contain 2 dark indigo bags, 3 muted magenta bags, 3 dull white bags.
dotted lime bags contain 4 shiny blue bags, 3 striped fuchsia bags.
posh brown bags contain 2 muted beige bags.
muted green bags contain 5 bright white bags, 5 dim gold bags.
vibrant salmon bags contain 1 pale green bag, 5 light maroon bags, 4 striped violet bags.
drab white bags contain 2 drab fuchsia bags, 4 dull beige bags, 2 pale coral bags, 1 shiny tan bag.
light lime bags contain 4 dotted salmon bags, 5 dark fuchsia bags, 2 vibrant indigo bags.
shiny tomato bags contain 5 wavy green bags, 2 striped blue bags, 3 faded green bags, 3 muted tomato bags.
mirrored aqua bags contain 2 dark gold bags, 2 shiny green bags.
plaid cyan bags contain 5 shiny brown bags, 2 pale aqua bags, 3 striped turquoise bags, 5 plaid yellow bags.
light crimson bags contain 3 bright silver bags, 2 dark lime bags.
dull cyan bags contain 3 pale gray bags, 5 light beige bags, 3 striped blue bags.
muted plum bags contain 2 muted turquoise bags, 5 wavy lavender bags, 3 striped blue bags, 3 striped gray bags.
posh tan bags contain 4 dark brown bags, 1 drab crimson bag.
clear yellow bags contain 3 striped purple bags, 4 faded blue bags.
wavy fuchsia bags contain 2 light beige bags, 3 faded fuchsia bags.
pale gold bags contain 4 faded green bags, 5 clear bronze bags, 5 vibrant aqua bags, 3 muted cyan bags.
shiny gray bags contain 3 plaid chartreuse bags.
bright indigo bags contain 3 drab fuchsia bags.
drab black bags contain 3 shiny brown bags, 3 posh blue bags.
dark crimson bags contain 5 faded olive bags, 1 mirrored green bag.
vibrant silver bags contain 1 dark black bag, 2 drab tan bags.
shiny green bags contain 4 dark plum bags, 4 drab fuchsia bags, 3 dim plum bags, 3 mirrored gold bags.
plaid crimson bags contain 1 dim olive bag, 5 bright brown bags, 5 dull lavender bags.
dark salmon bags contain 2 light gold bags, 4 shiny blue bags.
faded blue bags contain 4 striped crimson bags, 1 muted tomato bag.
wavy magenta bags contain 5 wavy purple bags, 3 bright yellow bags, 3 shiny maroon bags, 1 wavy orange bag.
striped cyan bags contain 1 dotted plum bag, 1 bright coral bag.
faded crimson bags contain 5 pale aqua bags, 3 light blue bags.
muted gray bags contain 3 shiny tomato bags.
striped aqua bags contain 3 dim crimson bags.
wavy salmon bags contain 5 drab bronze bags, 4 light maroon bags.
drab fuchsia bags contain 3 faded black bags, 4 shiny crimson bags, 5 shiny tan bags.
clear black bags contain 4 dark crimson bags, 5 pale lavender bags.
dotted orange bags contain 1 dotted coral bag, 1 shiny gold bag, 3 wavy coral bags.
plaid tomato bags contain 4 wavy orange bags.
dark white bags contain 3 posh cyan bags.
wavy lime bags contain 4 faded silver bags, 3 vibrant gold bags, 3 vibrant coral bags.
faded tomato bags contain 1 striped bronze bag, 4 dotted green bags.
mirrored salmon bags contain 1 faded crimson bag, 3 muted gold bags, 4 clear aqua bags.
drab maroon bags contain 5 clear silver bags, 4 vibrant cyan bags, 5 faded gold bags.
dull violet bags contain 4 shiny tomato bags.
bright orange bags contain 4 bright tan bags.
plaid magenta bags contain 3 light fuchsia bags.
shiny turquoise bags contain 5 muted bronze bags, 4 bright lavender bags, 4 dark tan bags.
pale fuchsia bags contain 4 dull crimson bags, 3 wavy red bags, 5 dark gold bags.
plaid fuchsia bags contain 2 dim cyan bags, 5 bright coral bags.
dark indigo bags contain 3 dotted teal bags, 3 striped blue bags.
vibrant bronze bags contain 4 mirrored plum bags, 5 faded silver bags.
light tomato bags contain 3 posh fuchsia bags, 4 mirrored magenta bags, 1 muted gold bag, 3 dim green bags.
shiny silver bags contain 2 dim yellow bags, 1 wavy coral bag.
bright bronze bags contain 3 plaid coral bags, 2 wavy coral bags, 2 bright gray bags.
plaid turquoise bags contain 3 dim lime bags.
plaid teal bags contain 1 vibrant teal bag, 3 dark indigo bags, 4 plaid fuchsia bags.
striped purple bags contain 2 striped chartreuse bags, 2 clear chartreuse bags, 4 dark cyan bags, 5 striped salmon bags.
pale orange bags contain 5 muted green bags.
light green bags contain 2 plaid plum bags.
plaid purple bags contain 4 muted lime bags.
dark cyan bags contain no other bags.
wavy teal bags contain 5 dull black bags, 3 striped teal bags, 4 dotted cyan bags, 5 vibrant olive bags.
shiny indigo bags contain 3 dull lavender bags.
bright beige bags contain 1 bright bronze bag.
light white bags contain no other bags.
muted red bags contain 3 light tan bags, 4 clear cyan bags.
light coral bags contain 2 dull aqua bags, 1 bright beige bag, 4 wavy maroon bags, 3 posh tan bags.
bright violet bags contain 2 drab beige bags, 3 shiny fuchsia bags, 2 shiny cyan bags, 5 light gray bags.
striped fuchsia bags contain 1 striped black bag, 4 shiny white bags, 3 dim plum bags.
vibrant teal bags contain 1 faded tomato bag, 3 dim gray bags.
striped turquoise bags contain 3 wavy silver bags, 3 bright orange bags, 5 plaid coral bags, 1 clear red bag.
mirrored fuchsia bags contain 1 dotted green bag, 1 plaid cyan bag.
dim green bags contain 1 posh olive bag, 1 dim silver bag.
faded orange bags contain 4 drab beige bags, 1 vibrant salmon bag, 2 plaid orange bags.
bright tomato bags contain 4 dim aqua bags, 2 posh beige bags, 4 striped purple bags.
faded lime bags contain 1 bright tan bag.
mirrored indigo bags contain 4 shiny tan bags, 3 faded blue bags.
vibrant orange bags contain 3 vibrant olive bags, 2 bright olive bags, 3 wavy violet bags.
plaid beige bags contain 2 shiny violet bags, 3 faded violet bags.
muted purple bags contain 3 light beige bags, 3 bright tan bags.
mirrored orange bags contain 5 plaid lime bags, 4 dotted olive bags.
wavy purple bags contain 3 dim chartreuse bags.
wavy blue bags contain 5 striped blue bags, 5 posh olive bags.
dull black bags contain 3 dotted plum bags.
drab bronze bags contain 5 dim olive bags, 3 vibrant gray bags, 3 pale green bags, 1 dull cyan bag.
pale coral bags contain 5 dim gold bags, 1 vibrant bronze bag.
dull orange bags contain 1 shiny turquoise bag.
mirrored gray bags contain 1 mirrored plum bag, 5 dim silver bags.
drab cyan bags contain 1 dark fuchsia bag, 1 striped salmon bag, 4 plaid beige bags, 5 dim olive bags.
dark bronze bags contain 2 pale salmon bags, 5 dull magenta bags, 5 clear indigo bags, 3 wavy plum bags.
dim tomato bags contain 5 striped lavender bags.
faded white bags contain 3 striped lime bags, 4 dotted orange bags.
dull teal bags contain 4 vibrant yellow bags.
clear teal bags contain 4 wavy gold bags.
muted tan bags contain 3 faded green bags.
dim gold bags contain no other bags.
dim turquoise bags contain 3 mirrored plum bags, 3 bright orange bags, 1 muted tan bag.
striped silver bags contain 4 dull lime bags, 5 striped blue bags.
striped yellow bags contain 2 vibrant crimson bags.
striped violet bags contain 1 clear beige bag, 2 dim indigo bags, 3 muted lime bags.
posh cyan bags contain 4 faded blue bags, 2 vibrant magenta bags, 3 dull lime bags, 3 shiny blue bags.
vibrant brown bags contain 5 shiny violet bags.
pale chartreuse bags contain 1 wavy teal bag, 1 muted maroon bag, 5 clear turquoise bags.
vibrant indigo bags contain 5 drab teal bags, 1 bright aqua bag.
bright green bags contain 4 drab silver bags, 5 shiny gold bags.
dim black bags contain 1 faded violet bag.
muted orange bags contain 3 dull yellow bags, 1 vibrant blue bag, 3 plaid tan bags, 2 dotted teal bags.
muted crimson bags contain 4 muted silver bags, 5 shiny lavender bags, 3 posh beige bags, 2 shiny purple bags.
clear tomato bags contain 4 dotted teal bags, 2 vibrant olive bags, 5 plaid magenta bags, 4 bright chartreuse bags.
vibrant fuchsia bags contain 5 dim cyan bags, 4 light white bags, 1 dull orange bag, 5 dark gold bags.
muted magenta bags contain no other bags.
dim brown bags contain 1 striped red bag, 4 posh fuchsia bags, 3 mirrored gold bags.
dim plum bags contain 1 vibrant turquoise bag, 1 clear chartreuse bag, 3 faded brown bags.
plaid gold bags contain 5 drab tomato bags.
wavy tomato bags contain 3 dark gold bags, 1 light orange bag, 4 muted salmon bags, 2 muted olive bags.
pale olive bags contain 2 plaid cyan bags.
wavy plum bags contain 4 faded aqua bags, 5 dull olive bags, 3 bright lavender bags, 2 drab chartreuse bags.
posh tomato bags contain 5 drab blue bags.
dull gray bags contain 5 dull olive bags, 3 mirrored coral bags, 4 striped lavender bags.
posh plum bags contain 5 dull cyan bags, 2 dotted orange bags, 3 plaid indigo bags, 5 light beige bags.
striped plum bags contain 2 drab white bags, 2 mirrored yellow bags, 3 dim crimson bags, 2 pale salmon bags.
light beige bags contain 3 dark cyan bags, 3 striped crimson bags.
dark maroon bags contain 5 light tan bags, 5 faded green bags, 3 striped gold bags, 4 bright aqua bags.
faded brown bags contain 5 dotted gold bags, 3 striped turquoise bags, 4 bright tan bags, 3 clear chartreuse bags.
striped lime bags contain 4 dim gold bags, 5 pale coral bags, 4 mirrored plum bags.
light olive bags contain 1 shiny white bag, 3 dotted plum bags, 3 clear orange bags, 3 posh turquoise bags.
light magenta bags contain 2 shiny turquoise bags.
dotted turquoise bags contain 5 posh olive bags.
dark violet bags contain 1 faded blue bag, 1 shiny green bag.
shiny plum bags contain 2 dotted blue bags, 1 clear gold bag.
striped bronze bags contain 5 dim chartreuse bags, 1 shiny violet bag.
vibrant lavender bags contain 1 faded fuchsia bag, 2 shiny blue bags, 2 dotted plum bags.
dotted crimson bags contain 2 dark cyan bags, 1 dim chartreuse bag, 4 light red bags.
posh blue bags contain 2 bright silver bags, 4 drab beige bags, 2 dim salmon bags.
plaid orange bags contain 3 dark lime bags.
wavy gold bags contain 1 drab olive bag, 1 shiny cyan bag, 3 drab brown bags.
muted lime bags contain 2 dull teal bags.
vibrant magenta bags contain 3 muted gray bags.
posh silver bags contain 4 bright lavender bags, 5 light gold bags, 2 posh beige bags, 2 dull crimson bags.
shiny bronze bags contain 5 pale lavender bags, 3 plaid bronze bags, 3 mirrored blue bags, 4 bright olive bags.
dotted tomato bags contain 2 drab yellow bags.
posh violet bags contain 4 muted fuchsia bags, 1 dark blue bag, 1 shiny indigo bag.
wavy turquoise bags contain 5 shiny yellow bags.
plaid lavender bags contain 3 dim lavender bags, 3 dotted salmon bags.
striped teal bags contain 5 mirrored crimson bags, 1 mirrored violet bag, 1 dark violet bag, 5 dotted yellow bags.
faded black bags contain 5 posh red bags.
faded tan bags contain 1 mirrored violet bag, 4 dark lime bags, 4 dim green bags, 4 muted green bags.
clear brown bags contain 3 pale coral bags, 1 plaid coral bag, 4 pale gray bags.
light violet bags contain 5 dim plum bags, 4 muted violet bags, 3 drab teal bags.
dotted gray bags contain 4 mirrored white bags, 3 vibrant lavender bags, 4 dark lime bags, 5 vibrant coral bags.
faded yellow bags contain 2 plaid bronze bags, 1 dark purple bag, 5 shiny crimson bags, 3 shiny tan bags.
shiny violet bags contain 4 dull lime bags, 4 muted white bags, 2 dark cyan bags.
faded gold bags contain 5 plaid aqua bags.
bright salmon bags contain 2 shiny lavender bags, 5 plaid red bags.
clear violet bags contain 4 posh turquoise bags.
light silver bags contain 1 light salmon bag, 2 clear aqua bags, 4 mirrored plum bags, 2 striped silver bags.
pale cyan bags contain 4 vibrant orange bags, 3 light salmon bags, 4 striped cyan bags, 4 wavy gray bags.
wavy cyan bags contain 3 light orange bags, 1 bright yellow bag, 2 pale fuchsia bags.
clear maroon bags contain 1 dotted coral bag, 4 plaid yellow bags.
striped blue bags contain 5 light white bags, 2 dull lime bags, 1 shiny maroon bag.
clear red bags contain no other bags.
pale tan bags contain 5 light gold bags, 5 dark brown bags, 1 wavy black bag, 5 drab blue bags.
mirrored magenta bags contain 4 dotted plum bags, 3 posh beige bags.
dull maroon bags contain 1 mirrored fuchsia bag.
dim silver bags contain 5 striped crimson bags, 1 light beige bag.
plaid olive bags contain 3 shiny white bags, 2 bright lavender bags.
shiny magenta bags contain 3 dotted gray bags, 1 shiny blue bag, 3 faded silver bags, 2 dark tomato bags.
mirrored green bags contain 4 dim cyan bags, 2 bright tan bags.
faded silver bags contain 1 dark plum bag, 5 dotted plum bags, 1 dark cyan bag, 5 dull red bags.
vibrant cyan bags contain 5 vibrant lavender bags.
shiny brown bags contain 4 striped blue bags, 1 light beige bag, 1 muted tan bag, 5 bright orange bags.
wavy maroon bags contain 3 vibrant white bags, 1 pale red bag, 5 striped yellow bags, 4 plaid bronze bags.
shiny aqua bags contain 5 dotted salmon bags, 5 bright maroon bags, 1 wavy red bag.
clear cyan bags contain 2 striped red bags, 5 plaid coral bags, 2 dark fuchsia bags.
dotted red bags contain 5 dim orange bags, 4 striped tan bags.
vibrant green bags contain 1 dark plum bag.
striped black bags contain 5 dull white bags.
dotted indigo bags contain 2 vibrant orange bags, 5 vibrant lavender bags, 4 shiny bronze bags.
dark tan bags contain 1 muted tan bag.
dotted yellow bags contain 3 dark cyan bags, 2 shiny maroon bags.
dull chartreuse bags contain 4 vibrant red bags, 4 dim salmon bags, 5 drab salmon bags.
shiny beige bags contain 3 dotted yellow bags, 2 muted tomato bags, 4 wavy red bags.
faded indigo bags contain 4 faded green bags.
light chartreuse bags contain 1 mirrored violet bag, 5 striped lavender bags.
dark red bags contain 5 dark green bags, 3 clear beige bags, 5 wavy tan bags, 4 striped cyan bags.
muted blue bags contain 3 dark beige bags, 2 bright lavender bags, 5 dull teal bags.
mirrored olive bags contain 5 dark lavender bags, 1 clear blue bag.
pale yellow bags contain 2 dark chartreuse bags, 4 posh silver bags, 2 dim crimson bags, 3 wavy gold bags.
dull brown bags contain 1 light aqua bag, 2 pale aqua bags, 1 faded red bag, 1 wavy white bag.
clear chartreuse bags contain 2 wavy coral bags.
bright white bags contain 4 light fuchsia bags, 5 drab turquoise bags, 5 striped lime bags.
light gray bags contain 4 mirrored violet bags, 5 dotted maroon bags, 3 pale lime bags.
mirrored cyan bags contain 4 mirrored salmon bags, 2 drab olive bags.
dark orange bags contain 3 vibrant lavender bags.
drab chartreuse bags contain 2 wavy orange bags.
muted white bags contain no other bags.
dull red bags contain 1 faded fuchsia bag, 2 dark purple bags, 4 clear red bags.
shiny red bags contain 2 bright gray bags, 4 drab blue bags, 2 bright aqua bags.
vibrant gold bags contain 3 shiny tan bags, 5 mirrored gold bags.
wavy red bags contain 1 dark plum bag, 3 striped blue bags, 4 light white bags, 1 wavy silver bag.
mirrored coral bags contain 4 dark indigo bags.
mirrored beige bags contain 1 muted white bag.
faded bronze bags contain 5 bright aqua bags, 2 dotted chartreuse bags, 2 faded tomato bags.
bright plum bags contain 3 drab chartreuse bags.
shiny coral bags contain 2 dark yellow bags, 5 dark blue bags, 4 dotted green bags.
mirrored yellow bags contain 1 dotted plum bag.
faded fuchsia bags contain no other bags.
bright magenta bags contain 4 muted orange bags, 3 striped red bags, 5 light bronze bags.
drab aqua bags contain 5 dotted indigo bags, 3 dim gray bags.
faded violet bags contain 2 shiny gold bags.
dull lavender bags contain 1 drab chartreuse bag, 2 shiny plum bags, 4 vibrant tan bags, 5 dark tomato bags.
shiny lavender bags contain 2 light fuchsia bags.
dotted brown bags contain 5 shiny brown bags, 4 light fuchsia bags, 3 plaid cyan bags.
dark olive bags contain 2 wavy red bags, 5 striped lavender bags, 4 vibrant lavender bags, 2 shiny gold bags.
dotted black bags contain 1 dark lime bag.
faded aqua bags contain 2 dim turquoise bags, 3 muted green bags, 5 clear aqua bags.
plaid yellow bags contain 1 striped turquoise bag, 4 striped lime bags.
pale bronze bags contain 4 muted tan bags, 5 dotted fuchsia bags.
muted coral bags contain 2 striped bronze bags, 1 dark violet bag.
dim indigo bags contain 1 shiny red bag.
drab gray bags contain 3 posh white bags, 2 plaid indigo bags.
pale silver bags contain 1 faded coral bag, 5 shiny lavender bags, 5 wavy lime bags.
wavy silver bags contain 1 vibrant bronze bag.
wavy crimson bags contain 1 mirrored orange bag.
dotted aqua bags contain 4 drab plum bags, 5 faded indigo bags, 3 dark violet bags, 3 pale gray bags.
mirrored violet bags contain 5 mirrored white bags.
dotted white bags contain 3 muted plum bags, 3 bright bronze bags, 2 dark salmon bags.
bright coral bags contain 5 mirrored gray bags.
dim aqua bags contain 3 mirrored plum bags, 3 plaid olive bags, 1 light gold bag.
drab crimson bags contain 5 faded purple bags.
pale crimson bags contain 4 dotted orange bags, 2 faded silver bags.
mirrored tan bags contain 3 posh gray bags, 2 dark silver bags, 3 dim tan bags.
clear olive bags contain 1 dim yellow bag, 1 bright blue bag, 3 bright tomato bags.
dim blue bags contain 3 drab black bags, 1 light blue bag, 5 light orange bags, 5 bright white bags.
mirrored chartreuse bags contain 4 drab beige bags, 1 pale indigo bag.
dark turquoise bags contain 1 vibrant black bag, 1 light turquoise bag, 5 pale aqua bags.
posh yellow bags contain 4 dim teal bags, 2 dark black bags.
clear aqua bags contain 2 drab teal bags, 5 light gold bags, 4 dim crimson bags.
dotted purple bags contain 4 striped salmon bags.
light indigo bags contain 3 faded red bags, 2 shiny crimson bags, 3 wavy green bags, 2 striped coral bags.
vibrant yellow bags contain 1 dotted cyan bag, 3 posh silver bags.
faded lavender bags contain 5 dull cyan bags.
dull magenta bags contain 2 dotted green bags.
posh indigo bags contain 1 dull lime bag, 4 striped lavender bags, 1 faded silver bag.
light aqua bags contain 3 posh maroon bags, 3 dotted black bags, 4 muted tomato bags, 4 mirrored magenta bags.
mirrored maroon bags contain 3 light aqua bags.
dim red bags contain 2 muted green bags, 1 vibrant tan bag.
wavy yellow bags contain 3 dotted cyan bags.
bright aqua bags contain 1 dotted maroon bag, 1 muted white bag, 3 striped turquoise bags.
clear fuchsia bags contain 2 mirrored fuchsia bags, 4 bright white bags, 3 mirrored white bags, 1 bright coral bag.
dotted olive bags contain 3 pale aqua bags, 4 light gold bags, 5 dim yellow bags.
light black bags contain 4 clear tan bags, 5 wavy lime bags, 3 dim fuchsia bags, 3 pale indigo bags.
dark purple bags contain 5 dark cyan bags.
dim purple bags contain 2 wavy crimson bags, 2 dim chartreuse bags, 3 shiny yellow bags, 1 light black bag.
plaid salmon bags contain 1 faded lime bag.
dotted cyan bags contain 2 shiny tomato bags, 1 mirrored plum bag.
posh maroon bags contain 1 light bronze bag, 4 muted tan bags, 5 vibrant plum bags.
dim fuchsia bags contain 3 dim plum bags, 5 dark gray bags.
bright tan bags contain 1 shiny maroon bag, 1 light beige bag, 2 faded fuchsia bags.
plaid green bags contain 3 wavy cyan bags, 5 dark chartreuse bags, 5 dark blue bags.
plaid black bags contain 4 dull olive bags, 4 mirrored white bags, 4 plaid white bags.
clear beige bags contain 1 dull tan bag.
mirrored tomato bags contain 5 drab tomato bags, 1 plaid bronze bag.
dim yellow bags contain 4 dark indigo bags, 4 bright silver bags, 3 muted purple bags.
clear tan bags contain 4 light gold bags, 3 bright lavender bags, 2 mirrored fuchsia bags.
dim lavender bags contain 3 vibrant aqua bags.
striped white bags contain 3 posh tomato bags, 3 dark gold bags, 2 clear olive bags, 1 dotted bronze bag.
wavy bronze bags contain 1 plaid lime bag, 4 plaid yellow bags, 1 bright white bag.
shiny orange bags contain 3 drab chartreuse bags, 1 shiny gold bag.
dim coral bags contain 2 faded silver bags.
bright gold bags contain 5 dim aqua bags, 2 drab bronze bags.
vibrant black bags contain 4 dotted green bags, 2 light brown bags.
bright teal bags contain 1 light gold bag, 2 bright aqua bags.
drab brown bags contain 2 wavy blue bags, 5 wavy orange bags.
dull yellow bags contain 4 striped green bags, 4 bright lime bags, 2 faded tan bags, 5 dotted green bags.
vibrant maroon bags contain 4 mirrored fuchsia bags.
vibrant gray bags contain 3 faded turquoise bags, 5 pale black bags, 3 drab aqua bags.
pale white bags contain 3 shiny beige bags.
dim beige bags contain 1 pale fuchsia bag, 1 muted lime bag, 3 dotted plum bags.
drab blue bags contain 4 dim crimson bags, 4 shiny beige bags, 2 bright silver bags.
dark black bags contain 5 light beige bags, 5 muted gold bags.
plaid bronze bags contain 3 wavy indigo bags.
posh salmon bags contain 3 dark salmon bags, 2 posh purple bags, 5 dim yellow bags.
mirrored lavender bags contain 4 wavy chartreuse bags, 4 plaid bronze bags.
muted brown bags contain 1 drab magenta bag, 2 vibrant plum bags, 4 clear purple bags, 4 dark blue bags.
wavy white bags contain 2 striped red bags.
dark gray bags contain 5 bright blue bags, 2 light brown bags.
mirrored silver bags contain 2 dotted chartreuse bags, 1 dotted fuchsia bag, 4 mirrored lavender bags, 2 mirrored white bags.
wavy brown bags contain 5 posh teal bags, 4 drab white bags, 5 shiny chartreuse bags, 4 light maroon bags.
posh gray bags contain 1 striped turquoise bag, 4 muted crimson bags, 3 clear yellow bags, 3 striped crimson bags.
dull tomato bags contain 5 drab purple bags, 4 faded yellow bags.
dotted blue bags contain 2 dull cyan bags, 3 dim plum bags.
vibrant tomato bags contain 5 plaid coral bags, 5 pale fuchsia bags.
wavy beige bags contain 3 dull magenta bags, 3 dotted beige bags, 3 bright white bags, 2 striped fuchsia bags.
plaid lime bags contain 3 light blue bags, 3 drab brown bags, 1 drab teal bag.
dim white bags contain 5 wavy coral bags, 5 vibrant bronze bags, 2 dark cyan bags, 2 dark plum bags.
bright yellow bags contain 4 pale aqua bags, 2 dim turquoise bags, 4 faded brown bags.
plaid maroon bags contain 1 dark teal bag, 4 vibrant white bags, 5 striped coral bags, 4 shiny white bags.
pale lavender bags contain 2 shiny violet bags.
drab magenta bags contain 5 bright gray bags.
clear salmon bags contain 4 wavy purple bags, 1 bright olive bag, 1 clear yellow bag.
dark yellow bags contain 1 bright bronze bag, 3 striped plum bags.
posh bronze bags contain 1 shiny maroon bag, 4 drab olive bags, 2 mirrored green bags, 5 light silver bags.
drab green bags contain 3 dim orange bags, 5 vibrant chartreuse bags.
light fuchsia bags contain 2 wavy silver bags, 4 muted white bags, 5 muted black bags, 1 faded green bag.
dark plum bags contain 4 bright tan bags, 4 dull lime bags, 2 faded fuchsia bags, 4 shiny maroon bags.
light teal bags contain 4 light lavender bags.
vibrant tan bags contain 1 vibrant bronze bag.
muted teal bags contain 5 wavy green bags, 5 plaid turquoise bags.
bright chartreuse bags contain 2 muted gold bags, 5 posh olive bags, 1 vibrant tan bag, 2 faded salmon bags.
dotted fuchsia bags contain 3 pale lime bags.
pale teal bags contain 5 plaid silver bags, 4 shiny turquoise bags, 3 dim coral bags, 2 vibrant bronze bags.
drab orange bags contain 2 shiny silver bags, 2 vibrant indigo bags, 5 mirrored lavender bags, 5 dark yellow bags.
clear green bags contain 4 vibrant beige bags, 1 bright crimson bag, 5 muted gray bags.
shiny yellow bags contain 4 light fuchsia bags, 2 mirrored plum bags.
plaid blue bags contain 4 mirrored blue bags, 1 plaid olive bag.
mirrored plum bags contain 2 dull red bags, 3 muted magenta bags.
dim bronze bags contain 3 vibrant olive bags.
posh green bags contain 3 mirrored blue bags, 4 vibrant yellow bags, 5 bright yellow bags, 2 wavy fuchsia bags.
clear blue bags contain 5 mirrored yellow bags.
dotted teal bags contain 5 shiny brown bags, 2 faded silver bags, 3 plaid coral bags.
muted cyan bags contain 4 clear aqua bags.
dark fuchsia bags contain 1 shiny blue bag, 1 dull fuchsia bag, 2 dull lime bags, 5 drab salmon bags.
dark silver bags contain 2 dim salmon bags.
muted beige bags contain 1 shiny lavender bag, 1 striped chartreuse bag.
dull indigo bags contain 1 bright beige bag, 2 dark gold bags, 1 mirrored magenta bag.
bright silver bags contain 3 faded violet bags, 4 dim cyan bags, 5 faded indigo bags, 1 clear chartreuse bag.
dim olive bags contain 1 mirrored plum bag, 1 clear indigo bag, 2 striped crimson bags.
pale magenta bags contain 5 vibrant black bags, 3 muted salmon bags, 1 dotted fuchsia bag.
faded turquoise bags contain 2 light lavender bags, 3 clear lavender bags, 3 dull coral bags.
posh gold bags contain 5 clear blue bags.
muted maroon bags contain 5 dark fuchsia bags, 2 muted red bags, 5 dim salmon bags.
muted tomato bags contain 4 striped blue bags, 3 dark plum bags, 5 faded green bags, 4 bright tan bags.
dark lime bags contain 2 posh white bags, 4 dull crimson bags, 2 dark cyan bags, 4 mirrored plum bags.
posh lime bags contain 1 wavy violet bag, 3 dotted teal bags, 5 shiny cyan bags.
light tan bags contain 4 striped turquoise bags, 4 dim white bags, 4 shiny violet bags.
dull bronze bags contain 2 drab teal bags, 5 light red bags, 4 muted indigo bags.
plaid coral bags contain 5 dark purple bags, 5 striped crimson bags, 4 light beige bags.
wavy lavender bags contain 5 muted white bags.
drab indigo bags contain 4 dotted green bags, 1 striped silver bag.
dull silver bags contain 1 dark yellow bag, 2 light beige bags, 3 striped indigo bags, 4 wavy violet bags.
dark aqua bags contain 1 drab violet bag.
muted bronze bags contain 4 clear chartreuse bags, 4 drab turquoise bags, 3 pale coral bags.
striped coral bags contain 1 shiny red bag, 1 dark purple bag.
faded beige bags contain 2 bright fuchsia bags, 2 mirrored turquoise bags.
dull plum bags contain 5 dull aqua bags.
drab lime bags contain 3 clear aqua bags, 4 shiny cyan bags.
pale plum bags contain 5 shiny silver bags, 5 dull coral bags.
pale violet bags contain 1 wavy purple bag, 1 light plum bag, 3 striped silver bags, 3 drab teal bags.
clear magenta bags contain 2 dark plum bags, 2 striped tan bags, 4 posh plum bags, 4 dark turquoise bags.
vibrant plum bags contain 3 dotted teal bags, 5 vibrant gold bags.
bright gray bags contain 3 muted white bags, 2 striped crimson bags, 3 mirrored gray bags, 4 wavy silver bags.
clear coral bags contain 2 vibrant magenta bags, 2 dim orange bags, 3 dark black bags.
vibrant chartreuse bags contain 3 dark lime bags, 1 mirrored turquoise bag, 2 vibrant indigo bags, 1 dull gray bag.
faded purple bags contain 2 mirrored indigo bags, 3 dark indigo bags, 2 pale fuchsia bags, 5 muted olive bags.
drab violet bags contain 4 muted black bags, 1 clear maroon bag, 1 clear gold bag.
dim magenta bags contain 5 wavy tan bags.
clear orange bags contain 5 shiny tomato bags, 1 faded fuchsia bag.
mirrored white bags contain 5 dim plum bags, 3 mirrored magenta bags.
plaid white bags contain 1 pale tomato bag, 2 posh magenta bags, 5 vibrant maroon bags, 5 shiny fuchsia bags.
shiny olive bags contain 4 striped salmon bags, 2 mirrored gray bags, 5 plaid beige bags.
plaid plum bags contain 3 bright bronze bags.
dull salmon bags contain 3 bright white bags, 2 muted cyan bags.
pale maroon bags contain 3 muted tan bags, 1 bright gray bag.
faded salmon bags contain 1 bright silver bag.
striped magenta bags contain 5 dark plum bags, 5 faded bronze bags, 4 striped brown bags.
vibrant crimson bags contain 2 muted lime bags, 5 plaid indigo bags.
wavy tan bags contain 2 shiny yellow bags, 3 clear beige bags, 2 dotted gold bags.
posh teal bags contain 4 striped gold bags, 3 drab salmon bags, 3 shiny plum bags, 2 pale gray bags.
dotted coral bags contain 2 wavy chartreuse bags, 3 wavy blue bags.
light purple bags contain 1 mirrored lime bag.
bright lavender bags contain 5 faded brown bags.
muted turquoise bags contain 2 shiny maroon bags, 3 light purple bags, 2 striped tan bags, 4 plaid cyan bags.
posh red bags contain 2 striped lavender bags, 1 dark black bag, 5 dark purple bags, 3 drab olive bags.
bright black bags contain 3 dark brown bags, 4 clear olive bags, 4 plaid olive bags.
mirrored bronze bags contain 1 wavy turquoise bag.
vibrant violet bags contain 2 plaid indigo bags, 4 faded orange bags.
drab tan bags contain 3 clear crimson bags, 4 mirrored turquoise bags, 2 muted magenta bags.
dim gray bags contain 5 striped black bags, 5 muted silver bags, 1 dotted blue bag, 3 posh gray bags.
dull tan bags contain 1 clear maroon bag, 4 posh beige bags, 2 striped crimson bags, 5 dim gold bags.
vibrant blue bags contain 4 bright beige bags, 5 bright bronze bags, 2 plaid salmon bags.
posh crimson bags contain 2 mirrored purple bags, 1 striped silver bag, 2 bright magenta bags, 5 bright blue bags.
dotted bronze bags contain 2 wavy crimson bags, 5 muted purple bags, 5 light gold bags.
pale brown bags contain 1 drab coral bag, 2 mirrored lavender bags, 4 dark tomato bags, 3 plaid indigo bags.
shiny maroon bags contain 5 light beige bags, 3 light white bags.
dark tomato bags contain 5 shiny gold bags, 5 clear aqua bags, 2 dotted gold bags.
dark beige bags contain 2 bright gray bags, 3 light beige bags, 1 dull lime bag.
light red bags contain 5 mirrored magenta bags, 1 mirrored lime bag, 4 dotted teal bags.
faded magenta bags contain 1 dim maroon bag, 3 mirrored gray bags, 1 dotted beige bag.
drab turquoise bags contain no other bags.
shiny salmon bags contain 5 shiny tan bags, 2 posh magenta bags, 4 clear turquoise bags.
dark magenta bags contain 1 light fuchsia bag, 3 muted yellow bags, 5 dotted olive bags, 4 dark crimson bags.
light gold bags contain 5 clear red bags.
faded red bags contain 4 clear beige bags, 3 dim silver bags, 4 posh gray bags.
pale salmon bags contain 5 mirrored white bags.
striped lavender bags contain 2 striped blue bags.
dull fuchsia bags contain 1 bright orange bag.
dull turquoise bags contain 1 vibrant tomato bag, 3 clear tan bags, 3 bright teal bags, 1 drab maroon bag.
dotted magenta bags contain 5 drab gold bags, 2 muted beige bags.
pale indigo bags contain 4 plaid brown bags, 1 plaid cyan bag, 1 mirrored black bag, 5 drab magenta bags.
drab yellow bags contain 5 dark turquoise bags, 2 dotted beige bags, 5 clear red bags, 2 muted lavender bags.
striped gray bags contain 5 bright orange bags, 5 muted white bags, 2 clear chartreuse bags.
dark lavender bags contain 5 dim gold bags, 2 pale coral bags.
dull gold bags contain 1 dull beige bag.
muted chartreuse bags contain 3 muted bronze bags, 1 faded black bag, 4 bright tan bags.
plaid chartreuse bags contain 4 dim indigo bags, 4 mirrored gold bags, 4 dim lime bags.
muted salmon bags contain 4 faded brown bags, 1 dotted black bag, 5 muted black bags.
bright purple bags contain 5 shiny red bags, 5 vibrant cyan bags, 4 plaid cyan bags, 5 bright silver bags.
dim chartreuse bags contain 1 faded indigo bag.
drab purple bags contain 4 muted cyan bags, 3 wavy lavender bags, 2 dotted blue bags."""
    main(myInput)
