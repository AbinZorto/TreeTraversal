import sys
import json
import networkx as nx
import matplotlib.pyplot as plt

with open(sys.argv[1], 'r') as f:
        dict_ = json.load(f)

dict_graph = nx.Graph(dict_)


def my_dfs_implementation(graph, origin, destination, already_visited = [], count=1, reverse=False):
  """
    Recursive way to implement DFS
  """
  # If I reach destination, I finish right here, return list with the final place
  if origin == destination:
    return [origin],count+1
  
  next_already_visited = already_visited.copy()
  # Add current place to already_visited
  next_already_visited.append(origin)
  
  neighbours = reversed(list(graph.neighbors(origin))) if reverse else graph.neighbors(origin)
  # Check all possible destinations from where I am
  for next_node in neighbours: 
    # Will only go if I havent gone before (No Loops nor going back)
    if next_node not in already_visited:
      # Go to first node possible
      result, count= my_dfs_implementation(graph, next_node, destination, next_already_visited, count, reverse)
      # If not dead end, means I found. Otherwise try next node
      if result != []:
        path = [origin] + result
        return path,count+1

  # If no node works, I return empty string which would mean dead end
  return [],count+1

path, _ = my_dfs_implementation(dict_graph, 'entrance', 'exit')
print(path)