'''This is the homework 1 for algorith thinking
 containing two parts : pepresenting directed graph
and computing degree distributions'''

# Representing directed graphs as shown
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]),
             3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
             7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    '''@param num_nodes is the number of nodes in the graph
        @return a directed graph with num_nodes nodes and all possible edges'''
    digraph = {}
    if num_nodes <= 0:
        return digraph  # return a empty graph if num_nodes is not positive
    fullset = set(range(num_nodes))
    for dummy_num in fullset:
        digraph[dummy_num] = fullset - set([dummy_num])
    return digraph


def compute_in_degrees(digraph):
    '''@param digraph a directed graph represted as adjacent list(dict)
        @return a dict with keys same as digraph and corresponding in degree'''
    indegree_dict = {}
	for dummy_key in digraph.keys():
		indegree_dict[dummy_key] = 0
    for dummy_val in digraph.values():
        for dummy_node in dummy_val:
            indegree_dict[dummy_node] = indegree_dict.get(dummy_node, 0) + 1
    return indegree_dict


def in_degree_distribution(digraph):
    '''@param digraph a directed graph represted as adjacent list(dict)
        @return a dict,keys as in-degree,val as number of nodes of that in-degree'''
    indegree_dist = {}
    indegree_by_nodes = compute_in_degrees(digraph)
    for dummy_val in indegree_by_nodes.values():
        indegree_dist[dummy_val] = indegree_dist.get(dummy_val, 0) + 1
    return indegree_dist



if __name__ == '__main__':
    print in_degree_distribution(EX_GRAPH1)
