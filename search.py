import graph

def bfs(g,end):
    q = [ g.root ]
    v = set()

    while not graph.Node.is_equal(q[0].state.arr,end.state.arr):
        v.add(q[0].state.arr)
        q[0].develop()
        q.extend([ child for child in q[0].children if child.state.arr not in v ])   
        q.pop(0)

    return q[0]

def dfs(g,end):
    s = [ g.root ]
    v = set()

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):
        v.add(s[0].state.arr)
        s[0].develop()
        r = s.pop(0)
        s = list([ child for child in r.children if child.state.arr not in v ]) + s

    return s[0]

def id(g,end):
    s = [ g.root ]
    v = set()
    limit = 1
    level = 0

    while not graph.Node.is_equal(s[0].state.arr,end.state.arr):
        if level < limit:
            v.add(s[0].state.arr)
            s[0].develop()
            level+=1

            r = s.pop(0)
            s = list([ child for child in r.children if child.state.arr not in v ]) + s
        else:
            s.pop(0)

        if len(s) == 0:
            limit += 1
            level = 0
            s = [ g.root ]
            v = set()

    return s[0]

