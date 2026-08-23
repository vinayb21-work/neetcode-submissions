class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            heapq.heappush(heap, x - y)
        return abs(heap[0])