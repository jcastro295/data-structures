'''

graph.py
--------

This module contains the Graph class, which is an implementation of the graph data structure.
'''

class Node:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

    def add_neighbors(self, v):
        self.neighbors.add(v)

class Graph:
    nodes= {}

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.nodes and v in self.nodes:
            self.nodes[u].add_neighbors(v)
            self.nodes[v].add_neighbors(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.nodes.keys())):
            print(key, sorted(list(self.nodes[key].neighbors)))


if __name__ == '__main__':

    g = Graph()
    a = Node('A')
    g.add_node(a)
    g.add_node(Node('B'))
    for i in range(ord('A'), ord('K')):
        g.add_node(Node(chr(i)))
        
    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    g.print_graph()