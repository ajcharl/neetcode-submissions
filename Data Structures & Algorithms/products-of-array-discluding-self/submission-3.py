class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]

        return output