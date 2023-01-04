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
    limit = 1
    level = 0
    
    s[0].prev = None

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):
        if level < limit:
            v.add(s[0].state.arr)
            s[0].develop()
            level+=1

            if len(s) > max_nodes_in_mem:
                max_nodes_in_mem = len(s)

            nodes_processed += 1
            r = s.pop(0)
            for child in r.children:
                if child.state.arr not in v:
                    child.prev = r
                    s = [ child ] + s
        else:
            s.pop(0)

        if len(s) == 0:
            limit += 1
            level = 0
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

#def astar(g,end)