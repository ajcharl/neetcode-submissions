class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    
        for word in t:
            if word in count:
                count[word] -= 1
            else:
                return False

        for word in count.values():
            if word != 0:
                return False
        return True