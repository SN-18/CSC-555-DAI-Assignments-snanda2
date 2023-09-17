import matplotlib.pyplot as plt
import networkx as nx

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
                d = {}                 # dictionary to store file data (each line)
                data.append([item.strip().strip(":") for item in line.split(' ')])





    counter = 0
    node_dict = dict()

    for li in data:
        G.add_nodes_from([li[0] for li in data])
        G1.add_nodes_from([li[0] for li in data])

    edges= list()

    for li in data:
        small_li = li[0]


        for j in range(1,len(li)):
            # small_li.append(li[j])

            edges.append([li[0],li[j]])

            G.add_edge(li[0],li[j])
            print("successfully added edge between nodes", li[0], li[j])

        G1.add_edges_from(edges)




        if G:
            print("G is not empty")
        else:
            print("G is an empty Graph, something went wrong")



    print("Gen_obj creation")

    if G:
        print("here")

    gen_obj = nx.find_cliques(G)
    print(*gen_obj, sep='\n')



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


        clustering_coefficients = {}
        clustering_coefficients = nx.clustering(G1.to_undirected())

        # Calculate the average clustering coefficient for the entire egonet
        average_clustering_coefficient = nx.average_clustering(G1.to_undirected())

        # Print clustering coefficients for each node
        print("Clustering Coefficients:")
        for node, cc in clustering_coefficients.items():
            print(f"Node {node}: {cc}")

        # Print the average clustering coefficient
        print(f"Average Clustering Coefficient: {average_clustering_coefficient}")

        clustering_coefficients = nx.clustering(G1.to_undirected())

        # Calculate the average clustering coefficient for the entire egonet
        clustering_coefficients = nx.clustering(G.to_undirected(), G.to_undirected())

        # Print clustering coefficients for each node
        print("Clustering Coefficients:")
        for node, cc in clustering_coefficients.items():
            print(f"Node {node}: {cc}")

        # Print the average clustering coefficient
        print(f"Average Clustering Coefficient: {average_clustering_coefficient}")



        elarge = [(u, v) for (u, v, d) in G.edges(data=True) ]
        # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 21]

        pos = nx.spring_layout(G, k=1)
        nx.draw_networkx_nodes(G, pos, node_size=100)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=1, edge_color='b')
        # nx.draw_networkx_edges(G, pos, edgelist=elarge,
        #                        width=1, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        plt.axis('off')
        plt.show()




