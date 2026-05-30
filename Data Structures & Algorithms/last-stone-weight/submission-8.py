class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            if stone1 == stone2:
                continue 
            else:
                heapq.heappush(maxHeap, stone1 - stone2)
        return -maxHeap[0] if maxHeap else 0