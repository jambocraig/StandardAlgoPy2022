import SortAlgorithms as s
import time as t

arr_1 = []
arr_2 = []
arr_3 = []
arr_4 = []
s.populate(arr_1, 2_000_000)
s.copy(arr_1, arr_2)
s.copy(arr_1, arr_3)
s.copy(arr_1, arr_4)
start_1 = t.time()
#s.bubble(arr_1)
stop_1 = t.time()
dur_1 = stop_1 - start_1
print(dur_1)
#print(arr_1)
start_2 = t.time()
#s.insertion(arr_2)
stop_2 = t.time()
dur_2 = stop_2 - start_2
print(dur_2)
#print(arr_2)
start_3 = t.time()
s.merge(arr_3)
stop_3 = t.time()
dur_3 = stop_3 - start_3
print(dur_3)
#print(arr_3)
start_4 = t.time()
arr_4 = s.quick(arr_4)
stop_4 = t.time()
dur_4 = stop_4 - start_4
print(dur_4)
#print(arr_4)

