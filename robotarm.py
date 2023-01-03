def move(w,p,r):
    arr = [list(arr) for arr in list(w.arr)]
    arr[r].append(arr[p].pop())
    arr = tuple(tuple(arr) for arr in arr)
    return arr

def add(w,p,box):
    w.arr[p].append(box)
    
    if box not in w.boxes:
        w.boxes[box] = {
            "position": p,
            "on_top": True
        }

    w.update()