__author__ = 'priya'

import kpeak_decomposition as kp
import networkx as nx


graphname = 'toygraph'
graphname = 'grad_links'


G = nx.read_edgelist(graphname+'.txt', delimiter=',', data=False)

# Draws mountain-plot as shown in the paper
kp.draw_mountainplot(G, graphname)

# Draws mountain-plot, including marking each mountain and each component in a mountain
kp.draw_mountainplot_components(G, graphname)

# Returns the peak numbers and core numbers of nodes
peaknumbers, corenumbers = kp.get_kpeak_decomposition(G)

