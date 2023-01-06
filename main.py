import warehouse;
import graph;
import search;
import tests;

import idastar

for i,case in enumerate(tests.cases):
    print('Testni primer: ', i)
    g = graph.Graph(warehouse.Warehouse(case['p'],case['n'], tuple([ tuple(arr) for arr in case['start']])))

    w2 = warehouse.Warehouse(case['p'],case['n'],tuple([ tuple(arr) for arr in case['end']] ))
    n2 = graph.Node([],[],w2)

    # DFS:
    #search.dfs(g,n2)
    
    # BFS:
    #search.bfs(g,n2)
    
    # ID:
    #search.id(g,n2)
    
    # IDA STAR:
    #ida = idastar.IdaStar(g,n2)
    #ida.find()
    #search.idastar(g,n2)

    # ASTAR:
    #search.astar(g,n2)