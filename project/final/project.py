import igraph as ig
import sys
import time

if len(sys.argv) < 2:
    print("Please provide the filename as an argument.")
    sys.exit(1)

filename = sys.argv[1]

def my_girvan(G, level):
    iteration = 0
    while(G.is_connected()):
        cpl = G.average_path_length()
        # print(level, iteration, cpl)

        betweenness = G.edge_betweenness()
        max_index = betweenness.index(max(betweenness))
        G.delete_edges(max_index)
        iteration += 1

    S = G.decompose(2)
    s0nodes = S[0].vcount()
    s1nodes = S[1].vcount()
    if (len(S) == 2):
        if (s0nodes > 1):
            print(level+1,s0nodes)
            my_girvan(S[0], level + 1)
        if (s1nodes > 1):
            print(level+1,s1nodes)
            my_girvan(S[1], level + 1)

# Create a graph from the edge list
graph = ig.Graph.Read_Edgelist(filename,directed=False)
tic = time.time()
print(0,graph.vcount())
my_girvan(graph, 0)
toc = time.time()
result = toc - tic

# print(result)
