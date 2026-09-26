class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left + 1
        seen = set()
        maximum_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                # throw away the window
                seen.remove(s[left])
                #tell left to jump tp the next index
                left += 1
            # th is is under the for loop, keep adding to right
            seen.add(s[right])
            # get the max length of the valid windows
            maximum_length = max(maximum_length, right - left + 1)
        
        return maximum_length
                
            