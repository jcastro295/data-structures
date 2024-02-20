'''

dfs.py
------

This module contains the dfs function, which is an implementation of the depth-first search algorithm.
'''


def dfs(graph:dict, node:str, visited:set):  #function for dfs 
    '''

    This function implements the Depth-First Search algorithm using recursion.

    Parameters
    ----------
    graph : dict
        dictionary to act as an adjacency list
    node : str
        node of the graph to start the search
    visited : set
        set to keep track of visited nodes of graph

    Returns
    -------
    None

    '''

    visited.add(node)
    print(node, end=" => ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


def dfs_objective(graph:dict, node:str, objective:str) -> bool:
    '''
    This function implements the Depth-First Search algorithm using a stack.

    Parameters
    ----------
    graph : dict
        dictionary to act as an adjacency list
    node : str
        node of the graph to start the search
    objective : str
        node of the graph to search for

    Returns
    -------
    bool
        True if the objective node is found, False otherwise
    '''

    stack = []
    visited = []
    stack.append(node)
    visited.append(node)

    while stack:
        m = stack.pop()
        print(f"{m}", end=" => ")
        if m == objective:
            return True
        for neighbor in graph[m]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)

    return False


if __name__ == '__main__':

    # Using a Python dictionary to act as an adjacency list
    graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }

    visited = set() # Set to keep track of visited nodes of graph.

    print("Following is Depth First Traversal: ")
    dfs(graph, '5', visited)
    print()
    print(dfs_objective(graph, '5', '4'))