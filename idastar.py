from collections import deque
import search
import math

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

        fscore = dist + search.evaluate(cur.state,self.end.state)

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
        bound = search.evaluate(self.g.root.state, self.end.state)

        while True:
            res = self.search(0,bound)

            if self.found:
                self.s.reverse()

                for i,child in enumerate(self.s):
                    if i > 0:
                        self.path_len += 1

                        for box in child.state.boxes:
                            if child.state.boxes[box]['position'] != self.s[i-1].state.boxes[box]['position']:
                                print([self.s[i-1].state.boxes[box]['position'],child.state.boxes[box]['position']])
                    
                    print(child.state.arr)

                print("statistika: ")
                print("st vozlisc v mem: ", self.max_nodes_in_mem)
                print("obdelanih vozlisc: ", self.nodes_processed)
                print("dolzina poti: ", self.path_len)

                break

            bound = res