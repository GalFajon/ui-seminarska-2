class Warehouse:
  def __init__(self,p,n,arr):
    self.p = p
    self.n = n
    
    self.boxes = dict()

    if arr:
      self.arr = arr
      for i,v in enumerate(arr):
        for j in arr[i]:
          self.boxes[j] = {
            "position": i,
            "on_top": False
          }
    else:
      self.arr =(() for i in range(0,p))

    self.update()

  def update(self):
    for box in self.boxes:
      for j,row in enumerate(self.arr):
        if box in row:
          self.boxes[box]["position"] = j

          if box == row[-1]:
            self.boxes[box]["on_top"] = True
          else:
            self.boxes[box]["on_top"] = False

  def to_string(self):
    swapped = [[' '] * self.p for i in range(0,self.n)]
    string = ''

    for i in range(0,len(self.arr)):
      for j in range(0,len(self.arr[i])):
        swapped[j][i] = self.arr[i][j]
  
    for i in reversed(range(0,len(swapped))):
      for j in range(0,len(swapped[i])):
        string += swapped[i][j] + ','
      
      string = string[0: -1]
      string += '\n'

    return string