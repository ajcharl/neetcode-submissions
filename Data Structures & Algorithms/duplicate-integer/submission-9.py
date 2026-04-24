class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()

        for num in nums:
            if num not in track:
                track.add(num)
            else: 
                return True
        return False

  