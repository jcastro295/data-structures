'''

graph_adj_matrix.py
-------------------

This module contains the Graph class, which is an implementation of the graph data structure using an adjacency matrix.
'''


class Node:
    def __init__(self, n):
        self.name = n


class Graph:
    nodes = {}
    edges = []
    edge_indices = {}

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[node.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.nodes and v in self.nodes:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' -> ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')    


if __name__ == '__main__':

    g = Graph()
    a = Node('A')
    g.add_node(a)
    g.add_node(Node('B'))
    for i in range(ord('A'), ord('K')):
        g.add_node(Node(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.print_graph()
    print(str(len(g.nodes)))