def move(w,p,r):
    arr = [arr.copy() for arr in w.arr]
    arr[r].append(arr[p].pop())

    return arr

def add(w,p,box):
    w.arr[p].append(box)
    
    if box not in w.boxes:
        w.boxes[box] = {
            "position": p,
            "on_top": True
        }

    w.update()