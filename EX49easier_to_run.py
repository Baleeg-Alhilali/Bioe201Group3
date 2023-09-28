#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict
# Define a function to perform topological ordering of nodes in a directed graph.
def topological_ordering(adj_list):
    # Create an empty set to store all unique nodes in the graph.
    nodes = set()
    # Initialize dictionaries to track in-degrees and out-degrees of nodes.
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    # Create a dictionary to represent the adjacency list of the graph.
    adjacency = defaultdict(list)

    # Parse the adjacency list and extract nodes and edges.
    for line in adj_list:
        node_from, neighbors_str = line.split(" -> ")
        node_from = int(node_from)
        neighbors = list(map(int, neighbors_str.split(",")))
        nodes.add(node_from)
        for node_to in neighbors:
            nodes.add(node_to)
            in_degree[node_to] += 1  # Increment in-degree of 'node_to'.
            out_degree[node_from] += 1  # Increment out-degree of 'node_from'.
            adjacency[node_from].append(node_to)  # Add the edge to the adjacency list.

    # Find nodes with no incoming edges (i.e., in-degree = 0) as the starting nodes for sorting.
    start_nodes = [node for node in nodes if in_degree[node] == 0]

    # Function to perform topological sorting using depth-first search.
    def topological_sort():
        visited = []  # List to store visited nodes in topological order.
        stack = start_nodes.copy()  # Initialize stack with starting nodes.

        while stack:
            current_node = stack.pop()
            visited.append(current_node)

            # Reduce the in-degree of each neighbor and add them to the stack if their in-degree becomes 0.
            for neighbor in adjacency[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        return visited

    # Perform topological sorting.
    topological_order = topological_sort()

    # Combine the result into the desired format as a comma-separated string.
    result = ", ".join(map(str, topological_order))

    return result

# Entry point for the program.
if __name__ == "__main__":
    # Example input in the given format.
    adj_list = [
        
    
  
        "0 -> 10,18,31,45,46",
        "1 -> 2,29,34",
        "10 -> 14,15,19,25,30",
        "11 -> 38",
        "12 -> 25,46",
        "13 -> 23,29,46",
        "14 -> 35",
        "15 -> 19,27,38",
        "16 -> 17,24,28,37",
        "17 -> 31",
        "18 -> 22,44",
        "19 -> 22,33,37,38",
        "2 -> 18,31,37,40",
        "20 -> 21,22,26,30",
        "21 -> 38,45",
        "22 -> 27,28",
        "23 -> 33",
        "25 -> 33",
        "26 -> 37",
        "27 -> 45",
        "28 -> 29",
        "29 -> 33,38",
        "3 -> 17,33,34,39",
        "30 -> 40",
        "31 -> 32,43",
        "32 -> 46",
        "34 -> 41",
        "39 -> 40",
        "4 -> 14,18,32,41,45",
        "41 -> 43",
        "44 -> 45,46",
        "45 -> 46",
        "5 -> 28,29,30,41",
        "6 -> 27,33,35",
        "7 -> 20,24,32,33",
        "8 -> 23,9",
        "9 -> 11,29,30,32,40,42"


    ]

    # Call the topological_ordering function to get the topological ordering.
    topological_order = topological_ordering(adj_list)

    # Print the topological ordering.
    print(topological_order)


# In[ ]:





# In[ ]:




