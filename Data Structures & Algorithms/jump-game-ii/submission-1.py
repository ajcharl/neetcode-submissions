class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        left = 0
        right = 0

        # keep making jumps until the right boundary reaches or passes the last tile
        while right < len(nums) - 1:
            farthest =  0

            # check every tile in the current window
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            # move to the next window
            left = right + 1
            right = farthest
            result += 1
            
        return result
