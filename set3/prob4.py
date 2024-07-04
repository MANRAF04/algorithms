import networkx as nx

a = [6, 5, 10, 4]
b = [4, 10, 3, 8]
c = [[0, 5, 0, 0],
    [5, 0, 6, 2],
    [0, 6, 0, 1],
    [0, 2, 1, 0]]

n = len(a)
G = nx.DiGraph()
for i in range(n):
    G.add_edge('S', i+1, capacity=b[i])
    G.add_edge(i+1, 'T', capacity=a[i])
    for j in range(n):
        if c[i][j] > 0:
            G.add_edge(i+1, j+1, capacity=c[i][j])

result, nodes = nx.minimum_cut(G, 'S', 'T')
print("Total cost: ", result)
prossesor1, prossesor2 = nodes
group1 = []
group2 = []
for node in prossesor1:
  if node != 'S':
    group1.append(node)
for node in prossesor2:
  if node != 'T':
    group2.append(node)

print("Jobs assigned to Processor 1: ", group1)
print("Jobs assigned to Processor 2: ", group2)