import warehouse;
import graph;
import search;

w = warehouse.Warehouse(3,3,[ ["A"],["B"],["C"] ])
g = graph.Graph(None,[],w)

w2 = warehouse.Warehouse(3,3,[ ['B','C','A'], [], [] ])
g2 = graph.Graph(None,[],w2)

print(search.id(g,g2).state.arr)