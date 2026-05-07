class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}

        for num in nums:
            if num not in track:
                track[num] = 1
            else:
                return True
        return False

