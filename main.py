import warehouse;
import graph;
import search;

g = graph.Graph(warehouse.Warehouse(3,3,( ("A"),("B"),("C") )))

w2 = warehouse.Warehouse(3,3,[ ['B','C','A'], [], [] ])
n2 = graph.Node(set(),set(),w2)

print(search.id(g,n2).state.arr)