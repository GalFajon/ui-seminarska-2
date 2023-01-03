import warehouse;
import robotarm;

class Graph:
  def __init__(self,initial):
    self.cache = dict()
    self.root = Node(set(),set(),initial,self)
  
  def cache_node(self,node):
    self.cache[node.state.arr] = node

class Node:
  def __init__(self,parents,children,state,graph=None):
    self.parents = parents
    self.children = children
    self.state = state
    self.graph = graph

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
        self.graph.cache[arr].parents.add(self)
        self.children.add(self.graph.cache[arr])
    else:
        n = Node(set([ self ]),set(),warehouse.Warehouse(self.state.p,self.state.n,arr),self.graph)
        self.children.add(self.graph.cache[arr])

  def develop(self):
    for box in self.state.boxes:
        if self.state.boxes[box]["on_top"] != False:
            possible_positions = [i for i in range(0,self.state.p) if i != self.state.boxes[box]["position"]]

            for pos in possible_positions:
                self.add(robotarm.move(self.state,self.state.boxes[box]["position"],pos))
