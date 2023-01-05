import warehouse;
import robotarm;

class Graph:
  def __init__(self,initial):
    self.cache = dict()
    self.distances = dict()
    self.root = Node([],[],initial,self)
  
  def cache_node(self,node):
    self.cache[node.state.arr] = node

  def develop_entire_graph(self):
    n = [ self.root ]
    v = { self.root.state.arr }

    while len(n) > 0: 
      n[0].develop()
      n.extend([child for child in n[0].children if child.state.arr not in v])
      v.add(n[0].state.arr)
      n.pop(0)

  @staticmethod
  def get_distance(start,end):
      q = [ start ]
      l = []
      n = 0
      v = set()

      while not Node.is_equal(q[0].state.arr,end.state.arr):
          v.add(q[0].state.arr)
          l.append(q.pop(0))
          
          if len(q) == 0:
              n += 1
              while len(l) > 0:
                  l[0].develop()
                  q.extend([ child for child in l[0].children if child.state.arr not in v ])
                  l.pop(0)   

      return n

  def calculate_distances(self):
    self.develop_entire_graph()
    nodes = list(self.cache.values())

    while len(nodes) > 0:
      cur = nodes.pop()

      wo = self.cache.copy()
      del wo[cur.state.arr]
      wo = list(wo.values())

      for node in wo:
        if (cur.state.arr,node.state.arr) not in self.distances and (node.state.arr,cur.state.arr) not in self.distances:
          self.distances[(cur.state.arr,node.state.arr)] = self.get_distance(cur,node)

class Node:
  def __init__(self,parents,children,state,graph=None):
    self.parents = parents
    self.children = children
    self.state = state
    self.graph = graph

    self.developed = False

    if self.graph is not None:
      self.graph.cache_node(self)
  
  @staticmethod
  def is_equal(state1,state2):
    for i in range(0,len(state1)):
        if len(state1[i]) != len(state2[i]): return False

        for j in range(0,len(state1[i])):
            if state1[i][j] != state2[i][j]: 
                return False
    
    return True

  def add(self,arr):  
    if arr in self.graph.cache.keys():
        if self not in self.graph.cache[arr].parents: self.graph.cache[arr].parents.append(self)
        if self.graph.cache[arr] not in self.children: self.children.append(self.graph.cache[arr])
    else:
        n = Node([ self ],[],warehouse.Warehouse(self.state.p,self.state.n,arr),self.graph)
        if self.graph.cache[arr] not in self.children:
           self.children.append(self.graph.cache[arr])

  def develop(self):
    for box in self.state.boxes:
        if self.state.boxes[box]["on_top"] != False:
            possible_positions = [i for i in range(0,self.state.p) if i != self.state.boxes[box]["position"]]

            for pos in possible_positions:
                self.add(robotarm.move(self.state,self.state.boxes[box]["position"],pos))
    
    self.developed = True
  
  def __lt__(self, other):
    return 0

  def __le__(self, other):
    return 0
