import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_visualization(G):
    centrality_vals = list((nx.betweenness_centrality(G, normalized=False)).values())
    degree_vals = [G.degree(i) for i in G.nodes()]
    nx.draw_networkx(G, node_size = [(item/20) for item in centrality_vals],
                     node_color = [item/10 for item in degree_vals], with_labels=False)
    plt.show()

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair. The output
# should be the number of vertices
def print_vertices(edgelist):
    vertices = []
    for item in edgelist:
        if item[0] not in vertices:
            vertices.append(item[0])
        elif item[1] not in vertices:
            vertices.append(item[1])
    print("Number of vertices: " + str(len(vertices)))

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair, and a vertex
# index that is an integer. The output should be the degree of
# the input vertex.
def print_degree(edgelist, v):
    degree = 0
    for item in edgelist:
        if int(item[0]) == v:
            degree+=1
        elif int(item[1]) == v:
            degree+=1

    print("Degree of vertex " + str(v) + ": " + str(degree))
    return degree

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair, and a vertex
# index that is an integer. The output should be the clustering
# coefficient of the input vertex.
def print_cluster_coefficient(edgelist, v):
    deg = print_degree(edgelist, v)
    v_list = []
    edges = 0
    # create a list of neighbor vertexes
    for i in edgelist:
        if int(i[0]) == v:
            v_list.append(i[1])
#    print("Neighbors of vertex",v,":",v_list)

    # find neighbors of v_list vertexes
    for i in edgelist:
        for j in v_list:
            if int(i[0]) == int(j):
                # compare if the neighbor is also a neighbor of 127
                for k in v_list:
                    if int(i[1]) == int(k):
                        if i[0] != i[1]:
                            edges+=1    # accounts for edges that self reference
#                        print(i)
    edges = int(edges/2)     # accounts for the fact that all edges are listed twice
    possible = int((deg*(deg - 1))/2)
    coeff = edges / possible

    print("Cluster Coefficient of vertex",v,"=",coeff,"or",edges,"/",possible)
    return coeff
    
# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair, and a vertex
# index that is an integer. The output should be the betweenness
# centrality of the input vertex.
def print_betweenness_centrality(edgelist, v):
    print("NEEDS IMPLEMENTATION")

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair. The output
# should be the average shortest path length of the graph.
def print_average_shortest_path(edgelist):
    print("NEEDS IMPLEMENTATION")

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair. The output
# should be the dense adjacency matrix of the graph.
def print_adjacency_matrix(edgelist):
    E = []
    with open("email-Eu-core.txt", "r") as file:
        for line in file:
            line = line.rstrip('\n')
            edge = line.split(' ')
            E.append(edge)
    graph_size = 1005
    # edge_matrix = np.matrix([ i for i in graph_size] ; [ j for j in graph_size])
    for edge in E:
        edge_string = str(edge[0])
        edge_string = edge_string.zfill(3)
        edge[0] = edge_string
        print(edge_string)

    # for edge in edgelist:
    #     edge_string = str(edge[0])
    #     edge_string = edge_string.zfill(3)
    #     edge[0] = tuple(map(int, edge_string.split(', ')))

    row = 0
    E.sort()
    for edge in E:
        row += 1
        print(edge)
    # print(edge_matrix)
    print("NEEDS IMPLEMENTATION")

def main():
    G = nx.MultiDiGraph()
    E = []
    vrt = 127               # Change to any vertex index
    
    with open("email-Eu-core.txt", "r") as file:
        for line in file:
            line = line.rstrip('\n')
            edge = tuple(line.split(' '))
            E.append(edge)            

    G.add_edges_from(E)
    # create_visualization(G)
    print_vertices(E)
    print_degree(E, vrt)
    print_cluster_coefficient(E, vrt)

    print_adjacency_matrix(E)
    # print(G.nodes)
    # print(nx.adjacency_matrix(G))


#    print_betweenness_centrality(E, vrt)
#    print_average_shortest_path(E)
#    print_adjacency_matrix(E)


main()
