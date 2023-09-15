
#use networkx inbuilt clustering
#kAGGLE dataset thats provided in assignment


######################################################################################################
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
#
#

import networkx as nx
G = nx.Graph()

# #
# # for i in range(4,1000):
# #     G.add_edge(i,i+
#
#
#
# lines = f.readlines()
# data = list()
#
#
# for line in lines:
#     line = line.strip() # remove leading/trailing white spaces
#
#     if line:
#         if i == 1:
#             columns = [item.strip() for item in line.split(' ')]
#             i = i + 1
#
#         else:
#             d = {} # dictionary to store file data (each line)
#             data.append([item.strip() for item in line.split(' ')])
#
# counter = 0
# node_dict = dict()
#
# for li in data:
#
#     print("li is:", li)
#
#     To be debugged
#     if counter<100:
#         print(li[0],li[1])
#         counter = counter + 1
#
#     for n, m in enumerate(li):
#         try:
#             n_int = node_dict[n]
#             m_int = node_dict[m]
#
#             print("successfully added edge between nodes", n_int, m_int)
#             G.AddEdge(n_int, m_int)
#         except:
#             print("For this edge, something happened, for now, let's debug")
#
# gen_obj = nx.find_cliques(G)
# print(gen_obj)
#
#
# print(*gen_obj, sep = "\n")
#



with open('0.egonet') as f:

    lines = f.readlines()             # list containing lines of file
    columns = []                      # To store column names
#
    i = 1
    data = list()

    #parsing
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces

        if line:
            if i == 1:
                columns = [item.strip() for item in line.split(' ')]
                i = i + 1

            else:
                d = {} # dictionary to store file data (each line)
                data.append([item.strip() for item in line.split(' ')])





    counter = 0
    node_dict = dict()

    for li in data:
        G.add_nodes_from([li[0] for li in data])

    # for j in range(1, len(li)):
    #     G.add_nodes_from([li[1] for li in data])

    edges= list()

    for li in data:
        # n,m = li[0], li[1]

        for j in range(1,len(li)):
            G.add_edge(li[0],li[j])
            print("successfully added edge between nodes", li[0], li[j])



        # for j in range(1,len(li)):
        #
        #     pass
        # for n, m in enumerate(li):

            # print("successfully added node", n)
        # node_dict[n]
        # print("n and m are:", n, m)

        # try:
        #     # n_int = node_dict[n]
        #     # m_int = node_dict[m]
        #     edges.append((n,m))




            # G.AddEdge(n, m)


            if G:
                print("G is not empty")
            else:
                print("G is an empty Graph, something went wrong")
        #
        # except:
        #     print("For this edge, something happened, for now, let's debug")
        # G.add_edges_from(edges)


    print("Gen_obj creation")
    if G:
        print("here")

    gen_obj = nx.find_cliques(G)
    print(*gen_obj, sep='\n')

    # gen_obj = nx.find_cliques(G)
    # print(*gen_obj, sep='\n')

    print("\n")
    print('Number of nodes', len(G.nodes))
    print('Number of edges', len(G.edges))


    if G:
        print("G is not empty")
        user = 0
        cliques = list(nx.find_cliques(G))
        print("Cliques in the social circle:")
        for i, clique in enumerate(cliques, 1):
            print(f"Clique {i}: {clique}")
        # cliques = k_cliques = dict()



        # for g in nx.algorithms.find_cliques(G):
        #
        #     if user not in cliques:
        #         cliques[user] = []
        #
        #     cliques[user].append(g)
        print("cliques: ", *cliques, sep=" ")


        # for g in nx.algorithms.community.label_propagation.asyn_lpa_communities(G):
        #     if user not in k_cliques:
        #         k_cliques[user] = []
        #     k_cliques[user].append(g)
        #     print("k_cliques: ", *k_cliques, sep=" ")




    # print("\n----- b. CCDF of centrality distribution for ", str(ds), "-----")
    print("\n1. degree_centrality(v) = d_v/(|N|-1) where d_v is Degree of node v and N is the set of all nodes:")

    centrality_deg = nx.degree_centrality(G)
    print("centrality_deg and nx.degree_centrality for Graph G, has been incorporated in formula")
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


    # print("\n5. eigenvector_centrality is given by Ax=λx where A is the adjacency matrix of the graph G with eigenvalue λ:")
    # centrality_eig = nx.eigenvector_centrality(G)
    # sorted_eig = {v: float(f"{c:0.2f}") for v, c in sorted(centrality_eig.items(), key=lambda item:item[1])}





    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import networkx as nx
#
# G = nx.Graph()
#
# # Load data from the file
# with open('facebook_combined.txt') as f:
#     lines = f.readlines()
#
# data = [line.strip().split() for line in lines if line.strip()]
#
# # Add nodes and edges to the graph
# for row in data:
#     node1, node2 = row[0], row[1]
#     G.add_node(node1)
#     G.add_node(node2)
#     G.add_edge(node1, node2)
#
# # Find cliques in the graph
# cliques = list(nx.find_cliques(G))
#
# # Print the cliques
# for i, clique in enumerate(cliques, 1):
#     print(f"Clique {i}: {clique}")
#
# # Print some statistics
# print("\nGraph Statistics:")
# print(f"Number of nodes: {len(G.nodes)}")
# print(f"Number of edges: {len(G.edges)}")
#
# # Calculate centrality measures
# degree_centrality = nx.degree_centrality(G)
# closeness_centrality = nx.closeness_centrality(G)
# betweenness_centrality = nx.betweenness_centrality(G, normalized=True, endpoints=False)
# pagerank_centrality = nx.pagerank(G, alpha=0.85)
# eigenvector_centrality = nx.eigenvector_centrality(G)
#
# # Print centrality measures
# print("\nCentrality Measures:")
# print(f"Degree Centrality: {degree_centrality}")
# print(f"Closeness Centrality: {closeness_centrality}")
# print(f"Betweenness Centrality: {betweenness_centrality}")
# print(f"Pagerank Centrality: {pagerank_centrality}")
# print(f"Eigenvector Centrality: {eigenvector_centrality}")

