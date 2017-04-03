__author__ = 'priya'

import peaklib.kpeak as kp
import networkx as nx


graphname = 'grad_links'

G = nx.read_edgelist(graphname+'.txt', delimiter=',', data=False)

kp.draw_mountainplot(G, graphname)
peaknumbers, corenumbers = kp.kpeak_decomposition(G)
print peaknumbers

