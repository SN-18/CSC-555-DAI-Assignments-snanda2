# Prosociality and Social Network Analysis 
## CSC-555 || Social Computing and DAI-Assignment P1 || snanda2

## Project P1, Question 2
Approaches used:

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


<li>Snap.cliques.h <br><br> 
</li>


</ul>




## Requirements
To install all the system requirements, on a command line interface such as Terminal for mac or Powershell for Windows, run:<br>

```pip : -r requirements.txt```<br>

## Instructions to execute

<ul>

<li>
Check the python version downloaded from the requirements.txt code on a terminal like environment (powershell for windows), using: <br>
  
  ```python --version ```
If it's python 3.X (X is an integer like 10,11,etc), proceed to the next step.
  
</li>
From an IDE like Pycharm, run the green icon at the top to start execution:

<br>
Or use, 

``` python ~/path/main.py```

<li>
  
</li>

<li>
  
</li>

<li>
  
</li>

</ul>


## Cliques, Clustering Coefficients, Measures of Centrality and Corresponding Graphs

### Clique List

<img width="1440" alt="Screenshot 2023-09-15 at 6 21 22 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/8482c4ec-87a2-4022-9e14-c2dd1fffaf6e"><p style="font-family:verdana" align='center'>Figure 1: Clique List </p>

<img width="810" alt="Screenshot 2023-09-17 at 2 33 23 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/1f8a3e92-b981-4ac9-94e4-39cbb81c3815"><p style="font-family:verdana" align='center'>Figure 2: Clique List </p>


### Clustering Coefficients

<img width="1440" alt="Screenshot 2023-09-15 at 7 20 22 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/9ae515ad-8453-4a1e-a0eb-8a341ead5c0d" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 3: Clustering Coefficients for Individual Nodes 1 </p><br>

<img width="1440" alt="Screenshot 2023-09-15 at 7 20 19 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/792b92b1-0591-4697-9d4a-2e6071f45bf8" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 4: Clustering Coefficients for Individual Nodes 2</p><br>

<img width="1440" alt="Screenshot 2023-09-15 at 7 20 09 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/54e51bfd-48e3-44f8-8c81-f0e4c61ad0ef" width="500" height="600" style="text-align: center;" class="center"><p style="font-family:verdana" align='center'>Figure 5: Clustering Coefficients for Individual Nodes 3</p><br>

### Run Outputs for Clustering per a Node's Social Circle

<img width="543" alt="Screenshot 2023-09-17 at 2 08 16 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/dcd7e115-0100-4eaf-b422-8257efcc0d15"> <p style="font-family:verdana" align='center'>Figure 6: Output for Run 1</p><br>

<img width="544" alt="Screenshot 2023-09-17 at 2 08 24 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/49d29a41-13e6-4258-bccc-845b7ae2bff9"> <p style="font-family:verdana" align='center'>Figure 7: Output for Run 2</p><br>


<img width="543" alt="Screenshot 2023-09-17 at 2 08 07 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/9e8e1882-0d57-422c-a0e5-9de92424d691"> <p style="font-family:verdana" align='center'>Figure 8: Output for Run 3</p><br>


<img width="540" alt="Screenshot 2023-09-17 at 2 08 37 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/8c6b3d26-f84b-454f-80f6-ac663b0e6e4c"> <p style="font-family:verdana" align='center'>Figure 9: Output for Run 4</p><br>

<img width="541" alt="Screenshot 2023-09-17 at 2 04 48 PM" src="https://github.com/SN-18/CSC-555-DAI-Assignments-snanda2/assets/83748468/3bfe45cd-3ebe-4bff-979d-515d80ee7d4f"> <p style="font-family:verdana" align='center'>Figure 10: Output for Run 5</p><br>


