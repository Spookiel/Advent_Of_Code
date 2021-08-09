import networkx as n
G = n.Graph()
G.add_edges_from([i.split(")") for i in open("i", "r").read().splitlines()])
print(sum(n.single_source_shortest_path_length(G, "COM").values()), n.shortest_path_length(G, "YOU", "SAN")-2)