class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        # sort by frequency descending, take first k
        result = sorted(count, key=count.get, reverse=True)
        return result[:k]   