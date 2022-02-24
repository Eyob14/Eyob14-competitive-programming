import heapq

q = int(input())
heap = []
heapq.heapify(heap)
deleted = {}
for i in range(q):
    Q = input().split()
    if len(Q) == 1 and Q[0] == "3":
        while (heap[0] in deleted) and (deleted[heap[0]] > 0) and (len(heap) != 0):
            deleted[heap[0]] -= 1
            heapq.heappop(heap)    
        print(heap[0])
    elif Q[0] == "1":
        heapq.heappush(heap, int(Q[1]))
    elif Q[0] == "2":
        if int(Q[1]) not in deleted:
            deleted[int(Q[1])] = 1
        else:
            deleted[int(Q[1])] += 1 
