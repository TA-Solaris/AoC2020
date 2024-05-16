### Advent of Code - Day 10 - Part 2 ###

### Defining Classes
class Graph():
    def __init__(self, myInput):
        ### Defining Properties
        self.nodes = [Node(0)]
        self.edges = []

        ### Passing Input to the build function
        self.build(sorted(list(map(int, myInput.splitlines()))))
    
    def __repr__(self):
        return f"{self.nodes} {self.edges}"
    
    def build(self, myInput):
        myInput.append(max(myInput) + 3)
        for value in myInput:
            newNode = Node(value)
            for node in self.nodes:
                if newNode.value - node.value in [1, 2, 3]:
                    self.edges.append(Edge(node, newNode))
            self.nodes.append(newNode)
    
    def getEdges(self, node):
        edges = set()
        for edge in self.edges:
            if edge.fro == node:
                edges.add(edge)
        return edges
    
    def bfs(self, target):
        queue = [self.nodes[0]]
        numRoutes = 0
        while queue:
            for e in self.getEdges(queue[0]):
                v = e.to
                if v.value == target:
                    numRoutes += 1
                queue.append(v)
            queue.pop(0)
        return numRoutes

class Node():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"

class Edge():
    def __init__(self, fro, to):
        self.fro = fro
        self.to = to
    
    def __repr__(self):
        return f"[{self.fro} {self.to}]"

### Defining Subroutines
def main(myInput):
    myGraph = Graph(myInput)
    print(myGraph.bfs(max(sorted(list(map(int, myInput.splitlines())))) + 3))

### Name Guard
if __name__ == "__main__":
    myInput = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    main(myInput)
