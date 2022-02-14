import heapq
class Solution:
    def HeapSolutionfindKthLargest(self, nums, k):
        '''
        Time Complexity = O(Nlogk)
        Space Complexity = O(k)
        '''
        return heapq.nlargest(k, nums)[-1]
            
    def BruteForcefindKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        max_heap = []
        for i in nums:
            max_heap.append(-1*i)
        heapq.heapify(max_heap)
        while k>1:
            heapq.heappop(max_heap)
            k -= 1
        return -1* heapq.heappop(max_heap)
        
