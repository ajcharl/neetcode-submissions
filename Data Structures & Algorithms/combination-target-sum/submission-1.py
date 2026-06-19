class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, current_sum):
            if current_sum == target:
                result.append(subset.copy())
                return
            
            if current_sum > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i, current_sum + nums[i])

            subset.pop()
            dfs(i + 1, current_sum)

        dfs(0, 0)
        return result
    
       

