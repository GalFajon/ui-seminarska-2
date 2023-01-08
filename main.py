import warehouse;
import graph;
import search;
import tests;

import time

for i,case in enumerate([ tests.cases[4] ]):
    print('------------------')
    print('Testni primer: ', i)
    print('------------------')

    g = graph.Graph(warehouse.Warehouse(case['p'],case['n'], tuple([ tuple(arr) for arr in case['start']])))

    w2 = warehouse.Warehouse(case['p'],case['n'],tuple([ tuple(arr) for arr in case['end']] ))
    n2 = graph.Node([],[],w2)

    #print("# DFS:")
    #start = time.time()
    #search.dfs(g,n2)
    #print("cas izvedbe: ", time.time() - start)

    #print("# BFS:")
    #start = time.time()
    #search.bfs(g,n2)
    #print("cas izvedbe: ", time.time() - start)

    #print("# ID:")
    #start = time.time()
    #search.id(g,n2)
    #print("cas izvedbe: ", time.time() - start)

    #print("# A STAR:")
    #start = time.time()
    #search.aStar.search(g,n2)
    #print("cas izvedbe: ", time.time() - start)
    
    print("# IDA STAR:")
    start = time.time()
    ida = search.IdaStar(g,n2)
    ida.find()
    print("cas izvedbe: ", time.time() - start)
