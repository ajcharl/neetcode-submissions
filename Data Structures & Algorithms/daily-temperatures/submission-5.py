class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for left in range(len(temperatures)):
            right = left + 1

            while right < len(temperatures) and temperatures[left] >= temperatures[right]:
                right += 1
            if right < len(temperatures):
                result.append(right - left)
            else:
                result.append(0)

        return result
