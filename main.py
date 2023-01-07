import warehouse;
import graph;
import search;
import tests;

for i,case in enumerate(tests.cases):
    print('------------------')
    print('Testni primer: ', i)
    print('------------------')

    g = graph.Graph(warehouse.Warehouse(case['p'],case['n'], tuple([ tuple(arr) for arr in case['start']])))

    w2 = warehouse.Warehouse(case['p'],case['n'],tuple([ tuple(arr) for arr in case['end']] ))
    n2 = graph.Node([],[],w2)

    print("# DFS:")
    search.dfs(g,n2)

    #print("# BFS:")
    #search.bfs(g,n2)

    #print("# ID:")
    #search.id(g,n2)

    #print("# A STAR:")
    #search.aStar.search(g,n2)
    
    #print("# IDA STAR:")
    #ida = search.IdaStar(g,n2)
    #ida.find()