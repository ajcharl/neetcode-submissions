class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        s1_Length = len(sorted_s1)

        for i in range(len(s2) - s1_Length + 1):
            window = s2[i : i + s1_Length]

            if sorted(window) == sorted_s1:
                return True
        return False


