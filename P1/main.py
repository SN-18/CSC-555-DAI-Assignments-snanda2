# https://networkx.org/documentation/stable/
# Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

import networkx as nx

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import snap



# v = snap.TIntV()

snap.TUNGraph.New()



#testing append menthod for a TIntV graph, works.
# v.append(1)
# print(len(v))
#end of testing it.


with open('gPlus_combined.txt') as f:

    lines = f.readlines()             # list containing lines of file
    columns = []                      # To store column names

    i = 1

    G1 = snap.TNGraph.New()

    # G1.AddNode(1)
    # G1.AddNode(5)
    #
    # G1.AddEdge(1, 5)

    print("printing G1, w u")
    print(G1)
    data = list()

    for line in lines:
        line = line.strip() # remove leading/trailing white spaces

        if line:
            if i == 1:
                columns = [item.strip() for item in line.split(' ')]
                i = i + 1

            else:
                d = {} # dictionary to store file data (each line)
                data.append([item.strip() for item in line.split(' ')])




                # for index in data:
                #     G1.AddNode(index)

                #We aren't doing this right now
                # for index, elem in enumerate(data):
                #     print(index,elem)
                #     G1.addNode(data[index])
                #     G1.addNode(index)
                #     d[columns[index]] = data[index]
                #     G1.AddNode(index,elem)
                #     v.append(1)
                #     v.append()
                #     G1.AddNode(1)

#checking if data contains the node pairs, as coded, works perfectly.
    # print(data)

#Testing creation of a small graph, works perfectly.
    # G1.AddNode(100)
    # G1.AddNode(200)
    # G1.AddEdge(100, 200)
    #
    # print("G1 is",G1)


    counter = 0
    node_dict = dict()

    for li in data:

        # print("li is:", li)

        #To be debugged
        # if counter<100:
        #     print(li[0],li[1])
        #     counter = counter + 1

        # for n,m in enumerate(li):
        #     print("n,m",n,m)
        #

        n = li[0]
        node_dict[n] = counter
        counter = counter + 1

            # print("n is:",n)

            # n_int = int(n)
            # print(n_int//10)

            # G1.AddNode(n_int//10)
            # G1.AddNode(int(li[1]))

        G1.AddNode(counter)

            # print("type of argument",type(m))

#let's wait a moment, will create edges li later.
        for n, m in enumerate(li):
            G1.AddEdge(node_dict(n), node_dict(m))




#let's wait a moment
    # for NI in G1.Nodes():
    #     for Id in NI.GetOutEdges():
    #         print("edge (%d %d)" %( NI.GetId(), Id))





# for i in range(len()):



def prepare_data(data):
    degreeCount = Counter(data)
    deg, cnt = zip(*degreeCount.items())
    cs = 1 - np.cumsum(cnt)/np.sum(cnt)
    return deg, cs


def ego_graph(G, n, radius=1, sample=-1.0, traversal='in', copy_attr=True):
    """PORTED FROM NETWORKX
    Returns induced subgraph of neighbors centered at node n within
    a given radius.

    Parameters
    ----------
    G : graph
      A NetworkX Graph or DiGraph

    n : node
      A single node

    radius : number, optional
      Include all neighbors of distance<=radius from n.

    center : bool, optional - NOT ADDED
      If False, do not include center node in graph

    undirected : bool, optional - NOT ADDED
      If True use both in- and out-neighbors of directed graphs.

    distance : key, optional - NOT ADDED
      Use specified edge data key as distance.  For example, setting
      distance='weight' will use the edge weight to measure the
      distance from the node n.

    sample : int/float, optional
      Number of nodes to sample as neighbors. Either positive int or float
      between 0.0 and 1.0.

    traversal : str, optional, either 'in', 'out', 'all'
      Get in, out or both ego neighborhoods

    copy_attr : bool, optional
      Copy node and edge attributes to ego graph
    """

    if traversal == 'in':
        if copy_attr:
            if sample != -1.0:
                if type(sample) is int:
                    if 0 > sample:
                        raise RuntimeError
                    else:
                        snapGraph = snap.GetInEgonetSubAttr(G._graph, n, radius, sample, -1.0)
                        return nx.nx.nx.sx.Graph(incoming_graph_data=snapGraph)
                else:
                    if not 0.0 <= sample <= 1.0:
                        raise RuntimeError
                    else:
                        snapGraph = snap.GetInEgonetSubAttr(G._graph, n, radius, 0, sample)
                        return nx.sx.Graph(incoming_graph_data=snapGraph)
            else:
                snapGraph = snap.GetInEgonetAttr(G._graph, n, radius)
                return nx.sx.Graph(incoming_graph_data=snapGraph)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError


def draw_plot(axcm, x, y, measures, typ, measure_name, xlabel, ylabel):

    axcm.plot(x, y, "ro")
    axcm.plot(x, y, "g-")
#
    if typ == "log-log":
        axcm.set_xscale("log")
        axcm.set_yscale("log")
#
    elif typ == "linear-log":
        axcm.set_yscale("log")

    axcm.set_title(measure_name + ": " + measures + " : " + typ)
    axcm.set_ylabel(ylabel)
    axcm.set_xlabel(xlabel)

#
# '''
#     code currently not in use
#     datasets.append("taro_village.txt") ,small dataset
#     datasets.append("lastfm_asia.txt") ,large dataset of 117.5MB
#     datasets.append("taro_village.txt") , small dataset
#     datasets.append("lastfm_asia.txt") , large dataset of 117.5MB
#
# '''

# print("what is happening?")
# if __name__ == '__main__':
#     print ('Mod2 UnitTest!')

    datasets = list()
    datasets.append("gplus_combined.txt")

    print("I'm inside main, the program has started")


    datasets = ["dolphins.txt"]  # small dataset

    for ds in datasets:
        print("\n\n", str(ds))
        print("----- a. CCDF for", str(ds), "-----")

        dataset = np.loadtxt(ds)
        G = nx.from_numpy_array(dataset)
        print("Current Dataset is:", ds)

      # G = nx.from_numpy_matrix(dataset)
      # print(ds, ":", nx.info(G))

        print('Number of nodes', len(G.nodes))
        print('Number of edges', len(G.edges))

        degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
        deg, cs = prepare_data(degree_sequence)
        f1, ax1 = plt.subplots(1, 3, figsize=(15,4.5))

        draw_plot(ax1[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "CCDF plot", "Degree", "P{D > d}")
        draw_plot(ax1[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "CCDF plot", "Degree", "P{D > d}")


        draw_plot(ax1[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "CCDF plot", "Degree", "P{D > d}")


        #remove print debug statements
        
        print("\n----- b. CCDF of centrality distribution for ", str(ds), "-----")
        print("\n1. degree_centrality(v) = d_v/(|N|-1) where d_v is Degree of node v and N is the set of all nodes:")

        centrality_deg = nx.degree_centrality(G)
        sorted_deg = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_deg.items(), key=lambda item:item[1])}


        print("\n2. closeness_centrality(v) = (|R(v)| / |N| - 1) * (|R(v)| / ∑{u belongs to R(v)} d(v, u)) where, R(v) is set of all nodes v can reach:")
        centrality_cls = nx.closeness_centrality(G)
        sorted_cls = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_cls.items(), key=lambda item:item[1])}


        print("\n3. betweenness_centrality(v) = ∑(sd(v)/sd{s, t}) where sd{s, t} is the number of shortest paths between nodes s and t. sd{s, t}(v) is the number of shortest paths between nodes s and t that pass through v:")
        centrality_bet = nx.betweenness_centrality(G, normalized = True, endpoints = False)
        sorted_bet = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_bet.items(), key=lambda item:item[1])}


        print("\n4. pagerank_centrality:")
        centrality_pgr = nx.pagerank(G, alpha = 0.85)
        sorted_pgr = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_pgr.items(), key=lambda item:item[1])}


        print("\n5. eigenvector_centrality is given by Ax=λx where A is the adjacency matrix of the graph G with eigenvalue λ:")
        centrality_eig = nx.eigenvector_centrality(G)
        sorted_eig = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_eig.items(), key=lambda item:item[1])}


        deg, cs = prepare_data([v for i, v in sorted_deg.items()])
        f2, ax2 = plt.subplots(1, 3, figsize=(15,4.5))

        print("I should be starting to draw plots - centrality/main.py")

        draw_plot(ax2[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "degree centrality", "Degree", "P{D > d}")
        draw_plot(ax2[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "degree centrality", "Degree", "P{D > d}")
        draw_plot(ax2[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "degree centrality", "Degree", "P{D > d}")


        deg, cs = prepare_data([v for i, v in sorted_cls.items()])
        f3, ax3 = plt.subplots(1, 3, figsize=(15,4.5))

        draw_plot(ax3[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "closeness centrality", "Degree", "P{D > d}")
        draw_plot(ax3[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "closeness centrality", "Degree", "P{D > d}")
        draw_plot(ax3[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "closeness centrality", "Degree", "P{D > d}")


        deg, cs = prepare_data([v for i, v in sorted_bet.items()])
        f4, ax4 = plt.subplots(1, 3, figsize=(15,4.5))
        draw_plot(ax4[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "betweenness centrality", "Degree", "P{D > d}")
        draw_plot(ax4[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "betweenness centrality", "Degree", "P{D > d}")
        draw_plot(ax4[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "betweenness centrality", "Degree", "P{D > d}")


        deg, cs = prepare_data([v for i, v in sorted_pgr.items()])
        f5, ax5 = plt.subplots(1, 3, figsize=(15,4.5))
        draw_plot(ax5[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "pagerank centrality", "Degree", "P{D > d}")
        draw_plot(ax5[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "pagerank centrality", "Degree", "P{D > d}")
        draw_plot(ax5[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "pagerank centrality", "Degree", "P{D > d}")


        deg, cs = prepare_data([v for i, v in sorted_eig.items()])
        f6, ax6 = plt.subplots(1, 3, figsize=(15,4.5))
        draw_plot(ax6[0], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-linear", "eigenvector centrality", "Degree", "P{D > d}")
        draw_plot(ax6[1], deg, cs, str(ds).strip(".txt").replace("_", " "), "log-log", "eigenvector centrality", "Degree", "P{D > d}")
        draw_plot(ax6[2], deg, cs, str(ds).strip(".txt").replace("_", " "), "linear-log", "eigenvector centrality", "Degree", "P{D > d}")






      # ac = nx.algebraic_connectivity(G)
      # print(ac)
      # print("I'm testing this")
      # plt.show()
      #

