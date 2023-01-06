import graph
import math
import heapq
from collections import deque

def bfs(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0

    # algo: 
    q = deque([ g.root ])

    v = set()
    cur = g.root

    g.root.prev = None

    while not graph.Node.is_equal(cur.state.arr,end.state.arr):
        cur = q.popleft()

        v.add(cur.state.arr)
        if not cur.developed: cur.develop()
        
        for child in cur.children:
            if child.state.arr not in v:
                child.prev = cur
                q.append(child)
        
        q.popleft()
        nodes_processed += 1

        if len(q) > max_nodes_in_mem:
            max_nodes_in_mem = len(q)

    # trace: 
    trace = cur
    seq = []

    while trace.prev is not None:
        seq.append(trace.state.arr)

        for box in trace.state.boxes:
            if trace.state.boxes[box]['position'] != trace.prev.state.boxes[box]['position']:
                seq.append([trace.prev.state.boxes[box]['position'],trace.state.boxes[box]['position']])

        trace = trace.prev
    
    seq.append(g.root.state.arr)

    for line in reversed(seq):
        print(line)

    #statistics:
    print("statistika:")
    print("st vozlisc v mem: ", max_nodes_in_mem)
    print("obdelanih vozlisc: ", nodes_processed)

    return q[0]

def dfs(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0

    # algo:
    s = deque([ g.root ])
    v = set()

    cur = g.root
    cur.prev = None

    while not graph.Node.is_equal(cur.state.arr,end.state.arr):
        cur = s.popleft()
        v.add(cur.state.arr)
        if not cur.developed: cur.develop()
        
        nodes_processed += 1
        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        for child in cur.children:
            if child.state.arr not in v:
                child.prev = cur
                s.appendleft(child)

    # trace:
    trace = cur
    seq = []

    while trace.prev is not None:
        seq.append(trace.state.arr)

        for box in trace.state.boxes:
            if trace.state.boxes[box]['position'] != trace.prev.state.boxes[box]['position']:
                seq.append([trace.prev.state.boxes[box]['position'],trace.state.boxes[box]['position']])

        trace = trace.prev
    
    seq.append(g.root.state.arr)

    for line in reversed(seq):
        print(line)

    # statistics:
    print("statistika:")
    print("st vozlisc v mem: ", max_nodes_in_mem)
    print("obdelanih vozlisc: ", nodes_processed)

    return s[0]

def id(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0

    #algo:
    s = deque([ g.root ])
    v = set()
    limit = 0
    
    cur = g.root
    cur.prev = None
    cur.level = 0

    while not graph.Node.is_equal(cur.state.arr,end.state.arr):  
        cur = s.popleft()

        v.add(cur.state.arr)

        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        nodes_processed += 1
        if not cur.developed: cur.develop()

        if cur.level <= limit:
            for child in cur.children:
                if child.state.arr not in v:
                    child.prev = cur
                    child.level = cur.level + 1
                    s.appendleft(child)

        if len(s) == 0:
            limit += 1
            s = deque([ g.root ])
            v = set()

    #trace:
    trace = cur
    seq = []

    while trace.prev is not None:
        seq.append(trace.state.arr)

        for box in trace.state.boxes:
            if trace.state.boxes[box]['position'] != trace.prev.state.boxes[box]['position']:
                seq.append([trace.prev.state.boxes[box]['position'],trace.state.boxes[box]['position']])

        trace = trace.prev
    
    seq.append(g.root.state.arr)

    for line in reversed(seq):
        print(line)

    #stats:
    print("statistika:")
    print("st vozlisc v mem: ", max_nodes_in_mem)
    print("obdelanih vozlisc: ", nodes_processed)

    return s[0]

def evaluate(state1,state2):
    s = 0

    for box in state1.boxes:
        if state1.boxes[box]['position'] != state2.boxes[box]['position'] or state1.boxes[box]['height'] != state2.boxes[box]['height']:
            s += 1
    
    return s

def astar(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0
    path_len = 0

    v = set()
    q = []
    
    heapq.heappush(q,(0,g.root))

    heuristics = dict()
    heuristics[g.root.state.arr] = 0 + evaluate(g.root.state,end.state)

    next = q[0][1]
    next.prev = None
    next.dist = 0

    # algo:
    while not graph.Node.is_equal(next.state.arr,end.state.arr):
        v.add(next.state.arr)

        nodes_processed += 1

        if len(q) > max_nodes_in_mem:
            max_nodes_in_mem = len(q)

        if not next.developed: next.develop()

        for child in next.children:
            if child not in v:
                if not hasattr(child,'prev'): child.prev = next
                child.dist = next.dist + 1

                val = child.dist + evaluate(child.state,end.state)

                if child.state.arr not in heuristics or val < heuristics[child.state.arr]:
                    heuristics[child.state.arr] = val
                    heapq.heappush(q,(val,child))
        
        next = heapq.heappop(q)[1]

    # trace:
    trace = next
    seq = []

    while trace.prev is not None:
        seq.append(trace.state.arr)
        path_len += 1

        for box in trace.state.boxes:
            if trace.state.boxes[box]['position'] != trace.prev.state.boxes[box]['position']:
                seq.append([trace.prev.state.boxes[box]['position'],trace.state.boxes[box]['position']])

        trace = trace.prev
    
    seq.append(g.root.state.arr)

    for line in reversed(seq):
        print(line)

    #stats:
    print("statistika:")
    print("st vozlisc v mem: ", max_nodes_in_mem)
    print("obdelanih vozlisc: ", nodes_processed)
    print("dolzina poti: ", path_len)

    return next