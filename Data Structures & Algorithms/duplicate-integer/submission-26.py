class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage  = {}

        for num in nums:
            if num not in storage:
                storage[num] = 1
            else:
                storage[num] += 1
        
        for value in storage.values():
            if value > 1:
                return True
        return False

