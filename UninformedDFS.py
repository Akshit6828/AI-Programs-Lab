def Check_Visited(visited_nodes, current_node):
    if current_node not in visited_nodes:
                visited_nodes.append(current_node)
                print(current_node , end=' -> ')

def Search_DFS (graph, start, destination):
    visited_nodes = []
    stack = [start]
    while stack:
            current_node = stack.pop()
            Check_Visited(visited_nodes,current_node)
            if current_node == destination:
                    return
            for adjacent_node in graph[current_node]:
                if adjacent_node not in visited_nodes:
                    stack.append(adjacent_node)


my_graph={'A':set(['B','C']),'B':set(['D','E']),'C':set(['F']),'D':set(['H']),'E':set([]),'F':set(['G']),'G':set([])}
print("DFS for graph: \n ", my_graph)
print("Path to be followed is")
Search_DFS(my_graph,'A','H')