class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr) 
        while len(arr) > 1:
            s1 = heapq.heappop(arr) 
            s2 = heapq.heappop(arr) 
            if s1 == s2:
                continue 
            else:
                heapq.heappush(arr, s1 - s2)
        return -arr[0] if arr else 0
