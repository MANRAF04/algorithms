import igraph as ig
from getNetworkEdges import getNetworkEdges
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
        print(level, iteration, cpl)

        betweenness = G.edge_betweenness()
        max_index = betweenness.index(max(betweenness))
        G.delete_edges(max_index)
        iteration += 1
        # if(iteration == 12):
        #     print(G.get_edgelist())
        #     print(G.is_connected())
        #     break

    S = G.decompose(2)

    if (len(S) == 2):
    #     if (nx.number_of_edges(S[0]) >= 1):
        if (S[0].vcount() > 1):
            my_girvan(S[0], level + 1)
        if (S[1].vcount() > 1):
            my_girvan(S[1], level + 1)

# edges,counts = getNetworkEdges(filename)
# print(edges)

# Create an empty graph
graph = ig.Graph.Read_Edgelist(filename,directed=False)
tic = time.time()
my_girvan(graph, 0)
toc = time.time()
result = toc - tic

print(result)