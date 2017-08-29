====================
k-peak decomposition
====================

This is the python code for performing k-peak decomposition and plotting mountain plots.

If using k-peak decomposition or the mountain-plot, please cite the following paper:

Priya Govindan, Chenghong Wang, Chumeng Xu, Hongyu Duan, Sucheta Soundarajan. The k-peak decomposition: Mapping the global structure of graphs.  WWW 2017

——————————————————

Graph Input: 
- Format: Undirected, unweighted graph in the form of a text file of comma separated edge-list. An example input file, ‘toygraph.txt’, is provided. 
- Reading the graph: The graph is to be read a Networkx graph. The file ‘sample_usage.py’ demonstrates how to read the input file and call the functions to compute k-peak decomposition and create mountain-plots.
- Note that we assume that every node has at least one edge. Singletons are removed before k-peak decomposition is done. Singletons have core and peak number of 0.
- Self-loops are ignored.


Required packages:
Networkx - https://networkx.github.io/
Matplotlib - http://matplotlib.org/


Key functions in ‘kpeak_decomposition.py’:

1. get_kpeak_decomposition : Given a graph, it computes the peak number of every node in the graph. Input is a a Networkx graph object. Output is a dictionary of core numbers and a dictionary of peak numbers. The keys in both dictionaries are node IDs and the values are the peak or core number.

2. draw_mountainplot : Given a graph, it creates the mountain-plot of the graph. Input is a a networkx graph object and a graph name in String. Output is a PDF file of the mountain-plot in the same directory as the code.

3. draw_mountainplot_components : Given a graph, it creates the mountain-plot of the graph. Input is a a networkx graph object and a graph name in String. Output is a PDF file of the mountain-plot in the same directory as the code.  draw_mountainplot_components differs from draw_mountainplot in that mountains with multiple components are depicted separately.

——————————————————
