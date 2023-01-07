from collections import deque
import math
import graph
import heapq

def evaluate(state1,state2):
    s = 0

    for box in state1.boxes:
        if state1.boxes[box]['position'] != state2.boxes[box]['position'] or state1.boxes[box]['height'] != state2.boxes[box]['height']:
            s += 1
    
    return s

def bfs(g,end):
    v = set()
    q = deque([ g.root ])

    g.root.prev = None

    max_nodes_in_mem = 0
    nodes_processed = 0
    path_length = 0

    while len(q) != 0:
        if len(q) > max_nodes_in_mem:
            max_nodes_in_mem = len(q)

        nodes_processed += 1

        cur = q.popleft()
        v.add(cur)
        
        if graph.Node.is_equal(cur.state.arr,end.state.arr):
            path = []

            while cur != None:
                path.append(cur.state)
                cur = cur.prev
                
            path.reverse()

            print(g.root.state.arr)

            for i,child in enumerate(path):
                path_length += 1

                if i > 0:
                    for box in child.boxes:
                        if child.boxes[box]['position'] != path[i-1].boxes[box]['position']:
                            print([path[i-1].boxes[box]['position'],child.boxes[box]['position'],child.arr])

            print("statistika:")
            print("dolzina poti: ", path_length)
            print("obdelana vozlisca: ", nodes_processed)
            print("stevilo vozlisc v spominu: ", max_nodes_in_mem)
        else:
            cur.develop()
            for child in cur.children:
                if child not in v:
                    child.prev = cur
                    v.add(child)
                    q.append(child)

def dfs(g,end):
    v = set()
    s = deque([ g.root ])

    g.root.prev = None

    max_nodes_in_mem = 0
    nodes_processed = 0
    path_length = 0

    while len(s) != 0:
        nodes_processed += 1
        
        if len(s) > max_nodes_in_mem:
            max_nodes_in_mem = len(s)

        cur = s[0]

        if graph.Node.is_equal(cur.state.arr,end.state.arr):
            path = []

            while cur != None:
                path.append(cur.state)
                cur = cur.prev
                
            path.reverse()

            print(g.root.state.arr)

            for i,child in enumerate(path):
                path_length += 1

                if i > 0:
                    for box in child.boxes:
                        if child.boxes[box]['position'] != path[i-1].boxes[box]['position']:
                            print([path[i-1].boxes[box]['position'],child.boxes[box]['position'],child.arr])

            print("statistika:")
            print("dolzina poti: ", path_length)
            print("obdelana vozlisca: ", nodes_processed)
            print("stevilo vozlisc v spominu: ", max_nodes_in_mem)
            return
        else:
            found = False
            cur.develop()

            for child in cur.children:
                if child not in v:
                    s.appendleft(child)

                    v.add(child)
                    if not hasattr(child,'prev'): child.prev = cur

                    found = True
                    break

            if not found:
                s.popleft()

def id(g,end):
    depth_limit = 1

    max_nodes_in_mem = 0
    nodes_processed = 0
    path_length = 0

    while True:
        v = set()
        s = deque([ g.root ])

        g.root.prev = None

        v.add(g.root)

        while len(s) != 0:
            nodes_processed += 1

            if len(s) > max_nodes_in_mem:
                max_nodes_in_mem += 1
            
            cur = s[0]

            if graph.Node.is_equal(cur.state.arr,end.state.arr):
                path = []

                while cur != None:
                    path.append(cur.state)
                    cur = cur.prev
                    
                path.reverse()

                print(g.root.state.arr)

                for i,child in enumerate(path):
                    path_length += 1

                    if i > 0:
                        for box in child.boxes:
                            if child.boxes[box]['position'] != path[i-1].boxes[box]['position']:
                                print([path[i-1].boxes[box]['position'],child.boxes[box]['position'],child.arr])

                print("statistika:")
                print("dolzina poti: ", path_length)
                print("obdelana vozlisca: ", nodes_processed)
                print("stevilo vozlisc v spominu: ", max_nodes_in_mem)
                return
            else:
                found = False
                
                cur.develop()

                if len(s) <= depth_limit:
                    for child in cur.children:
                        if child not in v:
                            s.appendleft(child)
                            v.add(child)

                            if not hasattr(child,'prev'): child.prev = cur

                            found = True
                            break

                if not found:
                    s.popleft()
        
        depth_limit += 1

class IdaStar:
    def __init__(self,g,end):
        self.g = g
        self.end = end
        self.heuristics = dict()

        self.s = deque([ g.root ])
        self.found = False
        self.v = set()
    
        self.max_nodes_in_mem = 0
        self.nodes_processed = 0
        self.path_len = 0

    def search(self,dist,bound):
        cur = self.s[0]

        self.nodes_processed += 1

        if len(self.s) > self.max_nodes_in_mem:
            self.max_nodes_in_mem = len(self.s)

        fscore = dist + evaluate(cur.state,self.end.state)

        if fscore > bound:
            return fscore
        
        if cur.state.arr == self.end.state.arr:
            self.found = True
            return fscore
        
        min = math.inf

        if not cur.developed: cur.develop()

        for child in cur.children:
            if child not in self.s:
                self.s.appendleft(child)

                res = self.search(dist + 1, bound)
                if self.found:
                    return res
                elif res < min:
                    min = res
                
                self.s.popleft()
        
        return min
    
    def find(self):
        self.s = deque([ self.g.root ])
        bound = evaluate(self.g.root.state, self.end.state)

        while True:
            res = self.search(0,bound)

            if self.found:
                self.s.reverse()
                
                print(self.g.root.state.arr)

                for i,child in enumerate(self.s):
                    if i > 0:
                        self.path_len += 1

                        for box in child.state.boxes:
                            if child.state.boxes[box]['position'] != self.s[i-1].state.boxes[box]['position']:
                                print([self.s[i-1].state.boxes[box]['position'],child.state.boxes[box]['position'],child.state.arr])
                    
                print("statistika: ")
                print("st vozlisc v mem: ", self.max_nodes_in_mem)
                print("obdelanih vozlisc: ", self.nodes_processed)
                print("dolzina poti: ", self.path_len)

                break

            bound = res

class aStar:
    def search(g,end):
        max_nodes_in_mem = 0
        nodes_processed = 0
        path_length = 0

        o = [ (0,g.root) ]
        c = set()

        g.root.prev = None

        g.root.g_score = 0
        g.root.f_score = evaluate(g.root.state,end.state)

        while len(o) != 0:
            nodes_processed += 1
            if len(o) > max_nodes_in_mem:
                max_nodes_in_mem = len(o)
            
            cur = heapq.heappop(o)[1]                        
            c.add(cur)

            if graph.Node.is_equal(cur.state.arr,end.state.arr):
                path = []

                while cur != None:
                    path.append(cur.state)
                    cur = cur.prev
                    
                path.reverse()

                print(g.root.state.arr)

                for i,child in enumerate(path):
                    path_length += 1

                    if i > 0:
                        for box in child.boxes:
                            if child.boxes[box]['position'] != path[i-1].boxes[box]['position']:
                                print([path[i-1].boxes[box]['position'],child.boxes[box]['position'],child.arr])

                print("statistika:")
                print("dolzina poti: ", path_length)
                print("obdelana vozlisca: ", nodes_processed)
                print("stevilo vozlisc v spominu: ", max_nodes_in_mem)
                return
            
            cur.develop()

            for child in cur.children:
                if child not in c:
                    dist = cur.g_score + 1

                    if not hasattr(child,'prev'):
                        child.prev = cur

                    if not hasattr(child,'g_score') or dist < child.g_score:
                        child.prev = cur
                        child.g_score = dist
                        child.f_score = dist + evaluate(child.state,end.state)

                    heapq.heappush(o,(child.f_score,child))
