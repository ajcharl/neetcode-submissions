class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]

            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

            max_freq = max(max_freq, count[char])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
        
            result = max(result, right - left + 1)
        return result