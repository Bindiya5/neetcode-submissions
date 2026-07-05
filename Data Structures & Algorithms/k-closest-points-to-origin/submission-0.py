class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for i in points:
            dist = (i[0] * i[0]) + (i[1] * i[1])
            minheap.append((dist,i[0],i[1])) 

        heapq.heapify(minheap)
        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(minheap)
            res.append([x,y])
        return res


        

        
