# -*- coding: utf-8 -*-
"""GP2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDT3cjiHX1Yn_fkWcwiBvadygj94F_4p
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

# NOTE: Code below allows the printout of the full sized Matrix for the adjacency Matrix
# np.set_printoptions(threshold=sys.maxsize)

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

    return degree

# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair, and a vertex
# index that is an integer. The output should be the clustering
# coefficient of the input vertex.
def print_cluster_coefficient(edgelist, v):
    deg = print_degree(edgelist, v)
    v_list = []
    edges = 0

    temp = nx.Graph()

    # create a list of neighbor vertices
    for i in edgelist:
        if int(i[0]) == v and i[1] not in v_list:
            temp.add_edge(i[0], i[1])
            v_list.append(i[1])
        elif int(i[1]) == v and i[0] not in v_list:
            temp.add_edge(i[0], i[1])
            v_list.append(i[0])

    # create_visualization(temp)
    
    # find neighbors of v_list vertices
    for i in edgelist:
      if i[0] in v_list and i[1] in v_list and i[0] != i[1]:
        edges+=1

    possible = int((deg*(deg - 1))/2)
    coeff = edges / possible

    # print("Cluster Coefficient of vertex",v,"=",coeff,"or",edges,"/",possible)
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
def print_average_shortest_path(edgelist, graph):
    # TODO: use breadth first search  and mark all nodes to find every vertex pair distance and then average
    total_average = 0

    vertices = graph.nodes
    for source_vertex in vertices:
        vertices_copy = vertices
        running_ave = 0
        for target_vertex in vertices_copy:
            if (source_vertex != target_vertex):
                running_ave += len(nx.shortest_path(graph, source_vertex, target_vertex)) - 1
        running_ave = running_ave / len(vertices)
        total_average += running_ave
    total_average = total_average/ len(vertices)
    print("Average shortest path: ", total_average)
    return total_average


# A function that takes the following input: a list of edges
# representing a graph, where each edge is a pair. The output
# should be the dense adjacency matrix of the graph.
def print_adjacency_matrix():
    # The reason that I am creating the graph in this function is that it is less of a headache to work with the str instead of a Tuple
    E = []
    # This includes the nodes that are self loops. It just won't mark them in the adjacency matrix
    nodeCount = 1005
    with open("email-Eu-core.txt", "r") as file:
        for line in file:
            line = line.rstrip('\n')
            edge = line.split(' ')
            E.append(edge)
    # initialize a matrix of size
    adjacency_matrix = np.zeros((nodeCount, nodeCount))
    # adding all edges to the adjacency matrix
    for edge in E:
        # Checking if the edge is a self loop. If not add a 1 to the adjacency matrix at x vertex and at the y vertex
        if edge[0] != edge[1]:
            adjacency_matrix[int(edge[0])][int(edge[1])] = 1
            adjacency_matrix[int(edge[1])][int(edge[0])] = 1

    # A compromise between printing the full matrix and a truncated one
    # for y in adjacency_matrix:
    #     print(y)

    # NOTE: If you want to print full adjacency matrix to check accuracy then uncomment the two lines of code at the beginning of the file
    print(adjacency_matrix)
    return adjacency_matrix

def main():
    G = nx.Graph()
    E = []
    vrt = 127               # Change to any vertex index
    
    with open("email-Eu-core.txt", "r") as file:
        for line in file:
            line = line.rstrip('\n')
            edge = tuple(line.split(' '))
            if (edge[0] != edge[1]):
                G.add_edge(edge[0], edge[1])


    E = G.edges



    # print(G.number_of_edges())
    # create_visualization(G)
    print_vertices(E)
    # print(G.number_of_nodes())
    print("Degree of vertex", str(vrt) + ":", print_degree(E, vrt))
    # print(G.degree[str(vrt)])
    print("Cluster Coefficient of vertex " + str(vrt) + ":", print_cluster_coefficient(E, vrt))


    # Adjacency Matrix Question
    print("NetworkX Adjacency Matrix: ")
    testMatrix = nx.adjacency_matrix(G)
    print(testMatrix.todense())
    print("\n", "Our Adjacency Matrix: ")
    print_adjacency_matrix()


    # print(nx.clustering(G, nodes=str(vrt)))
#    print_betweenness_centrality(E, vrt)

    print("Network x Average shortest path: ", nx.average_shortest_path_length(G))
    print("\n", "Our Average shortest path length")
    print(print_average_shortest_path(E, G))



main()
