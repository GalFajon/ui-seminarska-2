import warehouse;
import robotarm;

class Graph:
  def __init__(self,parent,children,state, root=None):
    self.parent = parent
    self.children = children
    self.state = state

    if root is not None: self.root = root
    else: self.root = self
  
  # Checks if two states on the graph are equal.
  @staticmethod
  def is_equal(state1,state2):
    for i in range(0,len(state1)):
        if len(state1[i]) != len(state2[i]): return False

        for j in range(0,len(state1[i])):
            if state1[i][j] != state2[i][j]: 
                return False
    
    return True

  # Adds new element if it is unlike parents or existing children.
  def add(self,new):
    parent = self.parent
    can_add = True

    while parent is not None:
        if Graph.is_equal(parent.state.arr,new.state.arr):
            can_add = False
            break
    
        parent = parent.parent

    for child in self.children:
        if Graph.is_equal(child.state.arr,new.state.arr):
            can_add = False
            break
    
    if can_add:
        self.children.append(new)

  def develop(self):
    for box in self.state.boxes:
        if self.state.boxes[box]["on_top"] != False:
            possible_positions = [i for i in range(0,self.state.p) if i != self.state.boxes[box]["position"]]

            for pos in possible_positions:
                s = warehouse.Warehouse(self.state.p,self.state.n,robotarm.move(self.state,self.state.boxes[box]["position"],pos))
                self.add(Graph(self,[],s, self.root))
