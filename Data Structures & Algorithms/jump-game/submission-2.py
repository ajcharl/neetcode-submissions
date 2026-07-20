class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jumpdistance = 0

        for i, jump in enumerate(nums):
            if i > max_jumpdistance:
                return False

            max_jumpdistance = max(max_jumpdistance, i + jump)
        return True
        