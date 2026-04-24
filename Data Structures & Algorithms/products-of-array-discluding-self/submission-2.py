class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            multiply = 1
            for j in range(0, len(nums)):
                if i != j:
                    multiply *= nums[j]
            results.append(multiply)
        return results