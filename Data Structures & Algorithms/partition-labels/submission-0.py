class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last = {}

        for i, letter in enumerate(s):
            last[letter] = i
        
        start = 0
        end = 0
        for i, letter in enumerate(s):
            end = max(end, last[letter])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result

        