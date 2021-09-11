import networkx as nx

graph = nx.Graph()
with open('input12.txt') as f:
    for l in f.readlines():
        g = l.strip().split()
        node, adj = g[0], g[1:]
        graph.add_edges_from((node, a) for a in adj)
print('Part 1:', len(nx.node_connected_component(graph, '0')))
print('Part 2:', nx.number_connected_components(graph))


