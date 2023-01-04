import warehouse;
import graph;
import search;

g = graph.Graph(warehouse.Warehouse(3,3,tuple([ tuple([]),tuple(["B"]),tuple(["A","C"]) ])))

w2 = warehouse.Warehouse(3,3,[ ['B','C','A'], [], [] ])
n2 = graph.Node(set(),set(),w2)

search.astar(g,n2)