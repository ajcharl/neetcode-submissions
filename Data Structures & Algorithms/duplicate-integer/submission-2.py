class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}

        for num in nums:
            if num in track:
                track[num] += 1
            else:
                track[num] = 1
        
        for num in track.values():
            if num > 1:
                return True 
        
        return False