class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-nums for nums in  nums]
        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)
