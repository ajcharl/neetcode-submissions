class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        far_reachable = 0

        for i in range(len(nums) - 1):
            far_reachable = max(far_reachable, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = far_reachable

        return jumps