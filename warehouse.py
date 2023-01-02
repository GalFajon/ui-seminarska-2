class Warehouse:
  def __init__(self,p,n):
    self.p = p
    self.n = n

    self.arr = [[] for i in range(0,p)]
  
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

    print(swapped)
    return string