import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

with open(sys.argv[1], 'r') as f:
        dict_ = json.load(f)

dict_graph = nx.Graph(dict_)


def bfs_implementation(graph, origin, destination, counter = 0, reverse=False):
  # Add current place to already_visited
  next_already_visited = [origin]
  # List of existent paths (for now only origin)
  total_paths = [[origin]] 

  # Will perform exploration of all current paths
  while len(total_paths)!= 0: 
    new_total_paths = []
    # I check every single existing path for now
    for path in total_paths:
      # Last element in path, where to go next?
      last_element_in_path = path[-1]
      # Nodes connected to here...
      nodes_found = list(reversed(list(graph.neighbors(last_element_in_path)))) if reverse else list(graph.neighbors(last_element_in_path))
      # Found destination!
      if destination in nodes_found:
        # Result complete, will return this path with destination at end
        return path + [destination], counter+1

      # Otherwise, I'll need to explore the nodes connected to here...
      for node in nodes_found:
        # I only will consider nodes not visited before (avoid loops and going back)
        if node not in next_already_visited:
          counter += 1
          # this node will be out of limits for next explorations
          next_already_visited.append(node)
          # I add this possible path for further exploration
          new_total_paths = new_total_paths + [path + [node]]
    # At the end, I need to explore only these "new" paths, until I reach destination, or run out of possible valid paths
    total_paths = new_total_paths

  # If no more possible paths, means solution does not exist
  return [],-1

bfs_path, _ = bfs_implementation(dict_graph, 'entrance', 'exit')
print(bfs_path)