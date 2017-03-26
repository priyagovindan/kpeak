# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:59:23 2017

@author: skiph
"""
import networkx as nx
import mountainplotlib.graph_cleanup as gcl
import mountainplotlib.main_mountain as mp
###########################

# maindir = '/Users/priya/Dropbox/CODE/rescore/'
# writedir = maindir +'/results/mountains2017/'
# datadir = maindir+'datasets/cleaned_formatted/'


maindir = ''
writedir = maindir +''
datadir = maindir+''
####################################



graphnames = ['grad_links_priya']


for graphname in graphnames:
    G = nx.read_edgelist(datadir+graphname+'.txt', delimiter=',', data=False)
    G.remove_edges_from(G.selfloop_edges())
    G = gcl.removeSingletons(G)

    print graphname, G.number_of_nodes(), G.number_of_edges()

    mp.compute_plotmountains(G, writedir, graphname)
