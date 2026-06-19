class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []    # backpack

        def dfs(i):
            # If we are done with the list, take a snapshot of whatever is in subset and append it to the result
            if i >= len(nums):
                result.append(subset.copy())
                return
                
            # To add to backpack(subset)
            subset.append(nums[i])
            dfs(i + 1)
            # To remove from backpack(subset)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result