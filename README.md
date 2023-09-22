# Prosociality and Social Network Analysis 
## CSC-555 || Social Computing and DAI-Assignment P1 || snanda2

## Project P1, Question 2
Approaches used:
<ol>
  
<li>
<u> Calculation of a representative clustering metric </u>, such as average clustering coefficient:<br><br>
<img width="128" alt="Screenshot 2023-09-17 at 2 44 28 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/63e1bd85-7d06-4a5f-969f-1ff276ee61f5"><br>

(Here the numerator is of the form C(P) and the Denominator is of the form L(p), where argument p denotes a high probability vertex in the graph, data structure.) 

<br>
</li>

<li>
<u> Centrality Measures: </u>

Historically first and conceptually simplest is degree centrality, which is defined as the number of links incident upon a node (i.e., the number of ties that a node has). The degree can be interpreted in terms of the immediate risk of a node for catching whatever is flowing through the network (such as a virus, or some information). In the case of a directed network (where ties have direction), we usually define two separate measures of degree centrality, namely indegree and outdegree.  

Centrality Measures: Centrality is defined as the importance, or how ‘central’ a node is, in a social-graph. A node that has high centrality, is expected to be of higher ‘importance’, where importance can be defined in several ways.     There are several measures of centrality which are useful: 

<li>
Simplest is degree centrality, which is defined as the number of links incident upon a node (i.e., the number of ties that a node has):  The degree centrality of a vertex v v, for a given graph, G := ( V , E ), with | V |,  |V| vertices and |E| edges, is defined as: <br>

<img width="154" alt="Screenshot 2023-09-22 at 1 07 30 AM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/ccf53f29-d231-4e9d-a866-7e63ab785e07"><br>

</li>

<li>The Betweenness Centrality is defined as the number of times a node acts as a bridge along
the shortest path, between two nodes A and B (say). In this theory, vertices that occur more frequently on a chosen path between two vertices, have a ‘high betweenness”.   If 𝛔st represents the total number of shortest paths from node s to node  and  t, and 𝛔st(v) is the number of those
paths that pass through v.  


It is given by the formula:     <br>

<img width="271" alt="Screenshot 2023-09-22 at 1 00 09 AM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/b6fbc567-6936-44dc-a4bd-3d7aa7a1be26"><br>
</li>


<li>
The Eigen-Vector Centrality, is defined as a measure of importance or influence of a node in a network, by measuring it’s transitive influence of nodes.    This implies that the nodes that are of ‘higher value’ contribute more weight to a node’s ‘importance’ than connections that are ‘low-value’.   av,t = 1, if vertex v is linked to vertex t, and av,t = 0 otherwise. The relative centrality score of vertex  xv, can be defined as:          <br>


<img width="305" alt="Screenshot 2023-09-22 at 12 58 05 AM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/05864fd7-6e96-495c-b148-92fe626f6664"><br>

</li>

</ol>


For more, please refer to: [P1](https://docs.google.com/document/d/1ShYEkktabqMvfDcdxB78NUmrM36nFrTM/edit)

Clustering using clique generation:

Libraries used:

<ul>

<li>
<u>Networkx:</u> NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks. It is used to study large complex networks represented in form of graphs with nodes and edges.<br>
  
More information: [Networkx Documentation](https://networkx.org/) <br><br>

</li>

<li><u>Matplotlib:</u> Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:<br><br>
  
```import matplotlib.pyplot as plt ```<br>
  
<u>More information:</u> [Matplotlib Documentation](https://matplotlib.org/)<br><br>

</li>



<li> SNAP Package: SNAP package supports large-scale graphs and networks. Graphs are data structures that can be used to describe complex abstractions such as topologies, social networks, physical phenomenon such as lattice sturctures, etc  and have a myriad applications. 

<br> In this context, a graph is represented as nodes with unique integer ids and directed/undirected/multiple edges between the nodes of the graph. Networks are graphs with data on nodes and/or edges of the network. Data types that reside on nodes and edges are simply passed as template parameters which provides a very fast and convenient way to implement various kinds of networks with rich data on nodes and edges. <br>

<u>More information:</u> [SNAP Documentation](http://snap.stanford.edu/) <br><br>

</li>


<li>Snap.cliques.h: Snap uses the inbuilt cliques.h which uses the clique percolation technique. The clique percolation method[1] is a popular approach for analyzing the overlapping community structure of networks. The term network community (also called a module, cluster or cohesive group) has no widely accepted unique definition and it is usually defined as a group of nodes that are more densely connected to each other than to other nodes in the network. 
More information can be found here: <br> 
  
  [CPM](https://en.wikipedia.org/wiki/Clique_percolation_method)
  
  <br><br> 
</li>


</ul>




 
## Instructions to execute

<ul>
<li>Clone the repository by using the command:<br>

```git clone https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2.git```</li>

<li>

<li>
  Install the software dependencies, and system requirementson:<br> 
  
  Open a command line interface such as Terminal for mac or Powershell for Windows, run<br>

```pip : -r requirements.txt```<br>

</li>
Check the python version downloaded from the requirements.txt code on a terminal like environment (powershell for windows), using: <br>
  
  ```python --version ```
If it's python 3.X (X is an integer like 10,11,etc), proceed to the next step.
  
</li>

<li>Navigate to the directory P1, using<br>
  
```cd /<path_name>/P1```

where, <path_name> is the path of the location where you cloned the github repo in step 1.

</li>

<li>
From an IDE like Pycharm, run the green icon at the top to start execution:

<br>
Or use, 

``` python ~/path/main.py```
</li>



<li>
  The output is produced as shown below. The graph is constructed based on data, the absolute measures (nodes and edges), centrality measures (degree,in-betweeness and eigen), and cliques based on Networkx's percolation method, are calculated as shown. The output is then depicted for several runs, to analyze graph complexity, node rank and the average clustering coefficient to depict the overall graph complexity.
</li>



</ul>


## Cliques, Clustering Coefficients, Measures of Centrality and Corresponding Graphs

### Clique List

<img width="1000" height="600" alt="Screenshot 2023-09-15 at 6 21 22 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/8482c4ec-87a2-4022-9e14-c2dd1fffaf6e"><p style="font-family:verdana" align='center'>Figure 1: Clique List </p>

<img width="1000" height="600" alt="Screenshot 2023-09-17 at 2 33 23 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/1f8a3e92-b981-4ac9-94e4-39cbb81c3815"><p style="font-family:verdana" align='center'>Figure 2: Clique List </p>


### Clustering Coefficients

<img width="1000" height="600" alt="Screenshot 2023-09-15 at 7 20 22 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/9ae515ad-8453-4a1e-a0eb-8a341ead5c0d" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 3: Clustering Coefficients for Individual Nodes 1 </p><br>

<img width="1000" height="600" alt="Screenshot 2023-09-15 at 7 20 19 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/792b92b1-0591-4697-9d4a-2e6071f45bf8" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 4: Clustering Coefficients for Individual Nodes 2</p><br>

<img width="1000" height="600" alt="Screenshot 2023-09-15 at 7 20 09 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/54e51bfd-48e3-44f8-8c81-f0e4c61ad0ef" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 5: Clustering Coefficients for Individual Nodes 3</p><br>

### Centrality Measures

<img width="1000" height="600" alt="Screenshot 2023-09-17 at 4 33 12 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/e0ec949b-1fb1-4ba3-8c6b-c45099fe5ef6"><p style="font-family:verdana" align='center'>Figure 6: Centrality </p><br>

<img width="1000" height="600" alt="Screenshot 2023-09-17 at 4 36 08 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/c0f9790a-1e56-4735-99dd-6b3e3c26597a"><p style="font-family:verdana" align='center'>Figure 7: In-Betweenness Centrality </p><br>

<img width="1000" height="600" alt="Screenshot 2023-09-17 at 4 36 50 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/69e99d99-a907-4182-9d6d-f9a09626066a"><p style="font-family:verdana" align='center'>Figure 8: Eigen-Vector Centrality </p><br>


### Run Outputs for Clustering per a Node's Social Circle

<img width="600" height="450"  alt="Screenshot 2023-09-17 at 2 08 16 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/dcd7e115-0100-4eaf-b422-8257efcc0d15" width="500" height="600"> <p style="font-family:verdana" align='center'>Figure 9: Output for Run 1</p><br>

<img width="600" height="450" alt="Screenshot 2023-09-17 at 2 08 24 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/49d29a41-13e6-4258-bccc-845b7ae2bff9" width="500" height="600"> <p style="font-family:verdana" align='center'>Figure 10: Output for Run 2</p><br>


<img width="600" height="450" alt="Screenshot 2023-09-17 at 2 08 07 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/9e8e1882-0d57-422c-a0e5-9de92424d691" width="500" height="600"> <p style="font-family:verdana" align='center'>Figure 11: Output for Run 3</p><br>


<img width="600" height="450" alt="Screenshot 2023-09-17 at 2 08 37 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/8c6b3d26-f84b-454f-80f6-ac663b0e6e4c" width="500" height="600"> <p style="font-family:verdana" align='center'>Figure 12: Output for Run 4</p><br>

<img width="600" height="450" alt="Screenshot 2023-09-17 at 2 04 48 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/3bfe45cd-3ebe-4bff-979d-515d80ee7d4f" width="500" height="600"> <p style="font-family:verdana" align='center'>Figure 13: Output for Run 5</p><br>

## Troubleshooting and Further Resources
<ol>
  <li>
    If you are unable to run the program, then firstly, check your system requirements. For this, quickly run:<br>

    ```pip freeze requirements.txt```

  <br> To validate if the requirements are installed, one can manually check version for any requirement, using:<br>
  
  ```requirement_name --version ``` <br>
 
  </li>


<li>
  If there is an issue with cloning or merging an older version, please refer:
 <ul> 
   
<br> <li> [Git Merge Help](https://git-scm.com/docs/git-merge) </li>
    <li> [Git Pull Help](https://git-scm.com/docs/git-pull) </li>
  
  </ul>
  
</li>

<li>
  If there is a problem with access: snanda2@ncsu.edu
</li>

</ol>


