"""
@author: Saurabh Nanda
@language : Python 3
@src file: main.py (driver)

@return: Runs analysis on public egonet.txt dataset, produces
a list of nodes, their cliques, and their 'importance',
based on three centrality measures, and an average coefficient
for understanding the overall graph complexity.

"""


###################################################################################################
import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.Graph()
G1 = nx.DiGraph()

with open('0.egonet') as f:

    lines = f.readlines()
    columns = []

    i = 1
    data = list()

    #parsing
    for line in lines:
        line = line.strip()


        if line:
            if i == 1:
                columns = [item.strip().strip(":") for item in line.split(' ')]
                i = i + 1

            else:
                d = {}                 #  store file data (each line)
                data.append([item.strip().strip(":") for item in line.split(' ')])




    num_nodes = len(data)
    counter = 0
    node_dict = dict()

    for li in data:
        G.add_nodes_from([li[0] for li in data])
        G1.add_nodes_from([li[0] for li in data])

    edges= list()

    for li in data:
        small_li = li[0]


        for j in range(1,len(li)):

            edges.append([li[0],li[j]])
            G.add_edge(li[0],li[j])

            print("successfully added edge between nodes", li[0], li[j])

        G1.add_edges_from(edges)



        #Quick Check
        if G:
            print("G is not empty")
        else:
            print("G is an empty Graph, something went wrong")


    #How does the graph look?
    print("Gen_obj creation")
    gen_obj = nx.find_cliques(G)
    print(*gen_obj, sep='\n')



    print("\n")

    #Number of nodes and edges
    print('Number of nodes', len(G1.nodes))
    print('Number of edges', len(G1.edges))

    #Cliques
    if G:
        user = 0
        cliques = list(nx.find_cliques(G))
        print("Cliques in the social circle:")



    #Coefficients for individual nodes
        clustering_coefficients = {}
        clustering_coefficients = nx.clustering(G1.to_undirected())
        length = dict(nx.all_pairs_shortest_path_length(G))


        # Avg. Coefficient for directed Graph
        average_clustering_coefficient = nx.average_clustering(G1.to_undirected())

        # Print clustering coefficients, for each node
        print("Clustering Coefficients:")

        # randomize using pseudo-generator
        rand_idx =random.randint(0,num_nodes+1)
        randomized_node_dict = G1.nodes.items()
        print(randomized_node_dict)

        base_node = None

        for element in randomized_node_dict:
            if rand_idx!=0:
                rand_idx = rand_idx - 1

            base_node = element




        i = 0
        print("base_node is:",base_node)
        for node, cc in clustering_coefficients.items():

            print(f"Node {node}: {cc}")
            i = i + 1


        #

        # Calculate the average clustering coefficient for the entire egonet, using UDG
        clustering_coefficients = nx.clustering(G.to_undirected(), G.to_undirected())

        # Print clustering coefficients for each node
        print("Clustering Coefficients:")
        for node, cc in clustering_coefficients.items():
            print(f"Node {node}: {cc}")

        # Print the average clustering coefficient
        print(f"Average Clustering Coefficient: {average_clustering_coefficient}")

        # Calculate Degree Centrality
        degree_centrality = nx.degree_centrality(G1)
        print("Degree Centrality:")
        for node, centrality in degree_centrality.items():
            print(f"Node {node}: {centrality}")

        # Calculate Betweenness Centrality
        betweenness_centrality = nx.betweenness_centrality(G1)
        print("\nBetweenness Centrality:")
        for node, centrality in betweenness_centrality.items():
            print(f"Node {node}: {centrality}")

        # Calculate Eigenvector Centrality
        eigenvector_centrality = nx.eigenvector_centrality(G1)
        print("\nEigenvector Centrality:")
        for node, centrality in eigenvector_centrality.items():
            print(f"Node {node}: {centrality}")


        edge_li = [(u, v) for (u, v, d) in G.edges(data=True)]


        pos = nx.spring_layout(G, k=1)
        nx.draw_networkx_nodes(G, pos, node_size=100)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=edge_li,
                               width=1, edge_color='b')

        # nx.draw_networkx_edges(G, pos, edgelist=elarge,
        #                        width=1, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        plt.axis('off')
        plt.show()




