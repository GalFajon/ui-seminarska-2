import warehouse;
import graph;
import search;
import tests;


for i,case in enumerate(tests.cases):
    print('Testni primer: ', i)
    g = graph.Graph(warehouse.Warehouse(case['p'],case['n'], tuple([ tuple(arr) for arr in case['start']])))

    w2 = warehouse.Warehouse(case['p'],case['n'],tuple([ tuple(arr) for arr in case['end']] ))
    n2 = graph.Node([],[],w2)

    search.bfs(g,n2)
    #search.dfs(g,n2)
    #search.id(g,n2)
    #search.astar(g,n2)
    #search.idastar(g,n2)