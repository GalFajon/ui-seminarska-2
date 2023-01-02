import warehouse;
import robotarm;
warehouse = warehouse.Warehouse(5,3)

robotarm.add(warehouse.arr,3,'A')
robotarm.add(warehouse.arr,3,'B')
robotarm.add(warehouse.arr,3,'C')
robotarm.add(warehouse.arr,4,'D')

print(warehouse.to_string())