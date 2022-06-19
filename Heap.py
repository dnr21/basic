from heapq import heappop, heappush  
 def heapsort(list1):  
     heap = []  
     for ele in list1:  
         heappush(heap, ele)  
     sort = []  
     while heap:   sort.append(heappop(heap))  
     return sort  
 list1 = [10,1,2,0,20]  
 print(heapsort(list1))
