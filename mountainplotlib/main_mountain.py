__author__ = 'priya'

import networkx as nx
from pylab import rcParams
rcParams['figure.figsize'] = 10,7
import matplotlib.pyplot as plt

def plot_mountains(node_CNdrops_mountainassignment_passed, orig_core_nums, peak_numbers, writedir, graphname):

    # 'node_to_plotmountain' is a dict with the mapping of each node to the mountain it is assigned for plotting.
    node_to_plotmountain = {}
    for n in node_CNdrops_mountainassignment_passed:
        node_to_plotmountain[n] = node_CNdrops_mountainassignment_passed[n][1]

    ### Part 1 ####
    # dict of dicts.
    # eg. permountain_ID_core_peak_numbers[0] is a dict of mountain 0.
    # Keys are nodes and value is a tuple <nodeID, corenumber, peak number>
    permountain_ID_core_peak_numbers = {}
    for n in node_to_plotmountain:
        if node_to_plotmountain[n] not in permountain_ID_core_peak_numbers:
            permountain_ID_core_peak_numbers[node_to_plotmountain[n]] = {}
        permountain_ID_core_peak_numbers[node_to_plotmountain[n]][n] = (n, orig_core_nums[n],peak_numbers[n])


    ### Part 2 ####
    #Sorting the nodes in each mountain
    #the final ordering is such that nodes are ordered in descending order of core number
    # the nodes with same core umber in a mountain are ordered (in descending order) or their peak number
    node_ordering_permountain = {}
    for id in permountain_ID_core_peak_numbers:
        mountaindict = permountain_ID_core_peak_numbers[id]
        unsorted_tuples = mountaindict.values()
        sortedbypeaknumber_tuples = sorted(unsorted_tuples, key=lambda xyv: xyv[2], reverse=True)
        sortedbyCOREnumber_tuples = sorted(sortedbypeaknumber_tuples, key=lambda xyv: xyv[1], reverse=True)
        node_ordering_permountain[id] = [x for x, y, z in sortedbyCOREnumber_tuples]

    ### Part 3 ####
    #Creating a list 'fullnodeordering' of nodeIDs ordered in the way to be plotted
    fullnodeordering = []
    for id in node_ordering_permountain:
        fullnodeordering.extend(node_ordering_permountain[id])

    ### Part 4 ####
    ## Arranging the values in arrays, of x and y axis to be plotted based on above ordering of 'fullnodeordering'
    x_vals = []
    y_vals = []
    y_vals2 = []
    for i in range(len(fullnodeordering)):
        x_vals.append(i)
        y_vals.append(orig_core_nums[fullnodeordering[i]])
        y_vals2.append(peak_numbers[fullnodeordering[i]])

    ### Part 5 ####
    ## the plotting
    ax = plt.gca()
    plt.fill_between(x_vals, y_vals, 0, color = 'lightblue', label = 'Area under the \'k-core number\' points')
    plt.plot(x_vals, y_vals, label = 'Core Number', color = 'blue')
    plt.scatter(x_vals, y_vals2, color = 'r', label = 'Peak Number')

    plt.ylabel('Core Number or Peak Number', fontsize=20); plt.xlabel('Individual nodes', fontsize=20)
    plt.legend(fontsize=18,bbox_to_anchor=(1.01, 1), prop={'size':18})
    plt.xlim(0, len(node_CNdrops_mountainassignment_passed.keys()))
    plt.ylim(0, max([orig_core_nums[x] for x in orig_core_nums]))
    ax.tick_params(axis='x', labelsize=18); ax.tick_params(axis='y', labelsize=18)
    # plt.show()

    plt.savefig(writedir+graphname+'_mountains_orderedByCoreThenPeakNumber_feb2017.png', bbox_inches='tight')

    plt.close()




def compute_plotmountains(G,writedir, graphname):
    # print graphname
    orig_core_nums = nx.core_number(G)
    print graphname, G.number_of_nodes(), G.number_of_edges(), max(orig_core_nums.values())
    print 'core nos computed'

    # Initializing node_CNdrops_mountainassignment
    # 'node_CNdrops_mountainassignment' is a dict where keys are nodeIDS
    # Each value is tuple of the maximum drop in core number observed for this node and the mountain to which it is assigned.
    node_CNdrops_mountainassignment = {}
    for n in G.nodes():
        node_CNdrops_mountainassignment[n] = [0, -1] #diff in core number, assignment to a mountain

    H = G.copy()
    H_nodes = set(G.nodes())

    current_core_nums = orig_core_nums.copy()
    current_d = max(current_core_nums.values())
    print 'current_d = ', current_d


    # 'current_plotmountain_id' keeps track of numbering of the plot-mountains
    current_plotmountain_id = 0
    peak_numbers = {}

    # Each iteration of the while loop finds a k-contour
    while(len(H.nodes()) > 0):

        # degen_core is the degeneracy of the graph
        degen_core = nx.k_core(H) # Degen-core

        # Note that the actual mountains may consist of multiple components.
        # To compute their core-periphery values or to analyze each component,
        # use the following line to find the components
        # res_core_comps = nx.connected_component_subgraphs(degen_core) #The comps in Degen-core
        # But in the mountain plot we plot the separate components related to a k-contour as a single mountain.
        # So, ignore the components for making mountain plots

        # Nodes in the k-contour. Their current core number is their peak number.
        kcontour_nodes = degen_core.nodes()
        for n in kcontour_nodes:
            peak_numbers[n] = current_core_nums[n]

        # Removing the kcontour (i.e. degeneracy) and re-computing core numbers.
        H_nodes = H_nodes.difference(set(kcontour_nodes))
        H = G.subgraph(list(H_nodes))
        new_core_nums = nx.core_number(H)


        for n in kcontour_nodes:
            # For the nodes in kcontour, its removal causes its core number to drop to 0.
            # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
            if current_core_nums[n] - 0 > node_CNdrops_mountainassignment[n][0]:
                node_CNdrops_mountainassignment[n][0] = current_core_nums[n]
                node_CNdrops_mountainassignment[n][1] = current_plotmountain_id


        for n in new_core_nums:
            # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
            if current_core_nums[n] - new_core_nums[n] > node_CNdrops_mountainassignment[n][0]:
                node_CNdrops_mountainassignment[n][0] = current_core_nums[n] - new_core_nums[n]
                node_CNdrops_mountainassignment[n][1] = current_plotmountain_id

        current_plotmountain_id += 1
        current_core_nums = new_core_nums.copy()


    print 'peak nos computed'

    plot_mountains(node_CNdrops_mountainassignment, orig_core_nums, peak_numbers, writedir, graphname)

###########################

# maindir = '/Users/priya/Dropbox/CODE/rescore/'
# writedir = maindir +'/results/mountains2017/'
# datadir = maindir+'datasets/cleaned_formatted/'
'''

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

    compute_plotmountains(G, writedir, graphname)
'''
