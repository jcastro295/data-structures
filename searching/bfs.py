'''

bfs.py
------

This module contains the bfs function, which is an implementation of the breadth-first search algorithm.

'''


def bfs(graph:dict, node:str): #function for BFS
    '''
    This function implements the Breadth-First Search algorithm.

    Parameters
    ----------
    graph : dict
        dictionary to act as an adjacency list
    node : str
        node of the graph to start the search
    '''

    visited = []
    queue = []  # FIFO struture    left to right in our queue

    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        print (m, end = " => ") 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def bfs_objective(graph:dict, node:str, objective:str):
    '''
    This function implements the Breadth-First Search algorithm using a queue.

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

    visited = []
    queue = []  # FIFO struture    left to right in our queue

    visited.append(node)
    queue.insert(0,node)
    
    while queue: # len(queue) !=0
        m = queue.pop() 
        print(f"{m}", end=" => ")
        if m == objective:
            return True
        for neighbor in graph[m]:
            if neighbor not in visited:
                queue.insert(0,neighbor)
                visited.append(neighbor)

    return False


if __name__ == '__main__':

    graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }

    print("Following is the Breadth-First Search")
    bfs(graph, '5')
    print()
    print(bfs_objective(graph, '5', '10'))


