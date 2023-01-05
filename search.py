import graph
import math

def bfs(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0

    # algo: 
    q = [ g.root ]
    v = set()
    
    g.root.prev = None

    while not graph.Node.is_equal(q[0].state.arr,end.state.arr):
        v.add(q[0].state.arr)
        q[0].develop()
        
        for child in q[0].children:
            if child.state.arr not in v:
                child.prev = q[0]
                q.append(child)
        
        q.pop(0)
        nodes_processed += 1

        if len(q) > max_nodes_in_mem:
            max_nodes_in_mem = len(q)

    # trace: 
    trace = q[0]
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
    s = [ g.root ]
    v = set()

    s[0].prev = None

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):
        v.add(s[0].state.arr)
        s[0].develop()

        r = s.pop(0)
        
        nodes_processed += 1
        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        for child in r.children:
            if child.state.arr not in v:
                child.prev = r
                s = [ child ] + s

    # trace:
    trace = s[0]
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
    s = [ g.root ]
    v = set()
    limit = 0
    
    s[0].prev = None
    s[0].level = 0

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):  
        v.add(s[0].state.arr)

        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        nodes_processed += 1
        r = s.pop(0)
        r.develop()

        if r.level <= limit:
            for child in r.children:
                if child.state.arr not in v:
                    child.prev = r
                    child.level = r.level + 1
                    s.insert(0,child)

        if len(s) == 0:
            limit += 1
            s = [ g.root ]
            v = set()

    #trace:
    trace = s[0]
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
        s += math.sqrt(math.pow(state1.boxes[box]['position'] - state2.boxes[box]['position'],2) + math.pow(state1.boxes[box]['height'] - state2.boxes[box]['height'],2))
    
    return round(s)

def distance(g,arr1,arr2):
    if (arr1,arr2) in g.distances:
        return g.distances[(arr1,arr2)]
    elif (arr2,arr1) in g.distances:
        return g.distances[(arr2,arr1)]
    elif arr2 == arr1:
        return 0

def astar(g,end):
    max_nodes_in_mem = 0
    nodes_processed = 0

    v = set()
    q = [ g.root ]

    heuristics = dict()
    heuristics[g.root.state.arr] = 0 + evaluate(g.root.state,end.state)

    next = q[0]
    next.prev = None
    next.dist = 0

    # algo:
    while not graph.Node.is_equal(next.state.arr,end.state.arr):
        v.add(next.state.arr)
        next.develop()

        n = [child for child in next.children if child.state.arr not in v]
        
        for child in n:
            child.prev = next
            if not hasattr(child,'dist'): child.dist = next.dist + 1
            heuristics[child.state.arr] = child.dist + evaluate(child.state,end.state)

        q.extend(n)

        if len(q) > max_nodes_in_mem:
            max_nodes_in_mem = len(q)

        min = math.inf
        
        for el in q:
            #if distance(g,g.root.state.arr,el.state.arr) + evaluate(el.state,end.state) < heuristics[el.state.arr]:
            #    heuristics[el.state.arr] = distance(g,g.root.state.arr,el.state.arr) + evaluate(el.state,end.state)
            
            if el.dist + evaluate(el.state,end.state) < heuristics[el.state.arr]:
                heuristics[el.state.arr] = el.dist + evaluate(el.state,end.state)

        for i,el in enumerate(q):
            if heuristics[el.state.arr] < min:
                min = heuristics[el.state.arr]
                next = el
                q.pop(i)
        
        nodes_processed += 1

    # trace:
    trace = next
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

    return next

def idastar(g,end):   
    max_nodes_in_mem = 0
    nodes_processed = 0

    #algo:
    s = [ g.root ]
    v = set()
    limit = 0
    
    heuristics = dict()
    heuristics[g.root.state.arr] = 0 + evaluate(g.root.state,end.state)
    
    bound = heuristics[g.root.state.arr] + 1
    newbound = bound

    s[0].prev = None
    s[0].dist = 0

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):  
        v.add(s[0].state.arr)

        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        nodes_processed += 1
        r = s.pop(0)
        r.develop()

        if heuristics[r.state.arr] < bound:
            for child in r.children:
                if child.state.arr not in v:
                    child.prev = r                    
                    child.dist = r.dist + 1
                    if child.state.arr not in heuristics or child.dist + evaluate(child.state,end.state) < heuristics[child.state.arr]:
                        heuristics[child.state.arr] = child.dist + evaluate(child.state,end.state)

                    s.insert(0,child)
        elif heuristics[r.state.arr] > bound:
            if newbound == bound or heuristics[r.state.arr] < newbound: 
                newbound = heuristics[r.state.arr]

        if len(s) == 0:
            bound = newbound
            limit += 1
            s = [ g.root ]
            v = set()

    #trace:
    trace = s[0]
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