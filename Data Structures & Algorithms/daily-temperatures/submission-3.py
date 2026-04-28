class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            days = 0
            found = False

            for j in range(i + 1, len(temperatures)):
                days += 1

                if temperatures[j] > temperatures[i]:
                    result.append(days)
                    found = True
                    break

            if not found:
                result.append(0)

        return result
