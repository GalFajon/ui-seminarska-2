import graph

def bfs(initial,end):
    q = [ initial ]

    while not graph.Graph.is_equal(q[0].state.arr,end.state.arr):
        q[0].develop()
        q.extend(q[0].children)   
        q.pop(0)

    return q[0]

def dfs(initial,end):
    s = [ initial ]

    while not graph.Graph.is_equal(s[0].state.arr,end.state.arr):
        s[0].develop()
        r = s.pop(0)
        s = r.children + s

    return s[0]

def id(initial,end):
    s = [ initial ]
    limit = 1
    level = 0

    while not graph.Graph.is_equal(s[0].state.arr,end.state.arr):
        if level < limit:
            s[0].develop()
            level+=1

            r = s.pop(0)
            s = r.children + s
        else:
            s.pop(0)

        if len(s) == 0:
            limit += 1
            level = 0
            s = [ initial ]

    return s[0]