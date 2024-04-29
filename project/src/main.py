import networkx as nx
import matplotlib.pyplot as plt

edges = [(1, 2), (2, 3), (3, 1), (3,4), (1,5)]

def  getNetworkEdges(filename):
  tuples = []
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
      for line in lines:
        # Split the line into words and remove trailing whitespace
        words = line.strip().split()
        # Create a tuple from the words and add it to the list
        tuples.append(tuple(words))
  except FileNotFoundError:
    print(f"Error: File {filename} not found.")
  return tuples

filename = "karateedges.txt"
karateEdges =  getNetworkEdges(filename)
# edw 8a jekinhsei h epanalhpsh
edgeMap = dict((edge,0) for edge in edges)
karateEdgeMap = dict((edge,0) for edge in karateEdges)
print(edgeMap)
G = nx.Graph()
G.add_edges_from(edges)
cpl = nx.average_shortest_path_length(G)
print("This is the cpl:", cpl)

sp = dict(nx.shortest_path(G))
print(sp)

for node in sp:
#   print(sp[node])
  for target in sp[node]:
    if target == node:
      print("yeah!")
      continue
    pairs = []
    for i in range(0, len(sp[node][target]) - 1):
        # Access elements with a step of 2 to create pairs
        pairs.append((sp[node][target][i], sp[node][target][i + 1]))
    print(pairs)
    for edge in pairs:
      if edge in edgeMap:
        edgeMap[edge] += 1
      else:
        edgeMap[edge[::-1]] += 1
    
# Sort edges by their responding value in edgeMap without saving the value
sortedEdges = sorted(edgeMap, key=edgeMap.get, reverse=True)
mostcomedge = sortedEdges[0]
sortedEdges = sortedEdges[1::]
G.remove_edge(*mostcomedge)
G.remove_edge(2,3)

print(edgeMap)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()