class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []  # Our physical backpack to hold the numbers


        def dfs(i, current_sum):
            # Rule 1: Success! Hit the exact target weight.
            if current_sum == target:
                result.append(subset.copy())  # Take a permanent snapshot
                return

            # Rule 2: Failure! Too heavy or ran out of numbers.
            if current_sum > target or i >= len(nums):
                return

            # Choice 1: Include the current number
            subset.append(nums[i])
            # Stay at index 'i' so we can reuse this number, update calculator
            dfs(i, current_sum + nums[i])

            # Choice 2: Exclude the current number (Cleanup & Move on)
            subset.pop()  # Take the number back out to reset our bag
            # Move map forward to next item, using our original untouched sum
            dfs(i + 1, current_sum)

        dfs(0, 0)  # Start at the first number with a sum of 0
        return result       