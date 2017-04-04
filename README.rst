Peak Package
=====

This package is the installable python package for peforming k-peak decomposition and plotting mountain plots. If using k-peak decomposition or the mountain-plot, please cite the following paper:

Priya Govindan, Chenghong Wang, Chumeng Xu, Hongyu Duan, Sucheta Soundarajan. The k-peak decomposition: Mapping the global structure of graphs.  WWW 2017


Installation
---
Required packages:
* Networkx - https://networkx.github.io/
* Matplotlib - http://matplotlib.org/

Please make sure the above packages are installed and enabled properly before you install the peak package.
Change your directory to the root folder of peak package, and use the following command to install the package:
> **python** setup.py install

After installation you can check the functionality of peak package by running the sample code scripts.
Sample script is located at folder **sample_code/**.

Usage
---
Sample usage:
Import peak package to include all functionalities in peak package, import code as follow:

> **import** peak.kpeak as kp

Graph Input:
- Format: Undirected, unweighted graph in the form of a text file of comma separated edge-list. An example input file, ‘toygraph.txt’, is provided.
- Reading the graph: The graph is to be read a Networkx graph. The file ‘sample_usage.py’ demonstrates how to read the input file and call the functions to compute k-peak decomposition and create mountain-plots.
- Note that we assume that every node has at least one edge. Singletons are removed before k-peak decomposition is done. Singletons have core and peak number of 0.
- Self-loops are ignored.




Key functions in ‘kpeak_decomposition.py’:

1. get_kpeak_decomposition : Given a graph, it computes the peak number of every node in the graph. Input is a a Networkx graph object. Output is a dictionary of core numbers and a dictionary of peak numbers. The keys in both dictionaries are node IDs and the values are the peak or core number.

2. plot_mountains_given_mountainassignment : Given a graph, it creates the mountain-plot of the graph. Input is a a networkx graph object and a graph name in String. Output is a PDF file of the mountain-plot in the same directory as the code.

——————————————————
