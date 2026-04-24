class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in storage:
                return[storage[remainder], i]
            else:
                storage[nums[i]] = i