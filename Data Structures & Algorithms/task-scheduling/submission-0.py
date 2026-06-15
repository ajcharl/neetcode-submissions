class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        frequencies = list(counts.values())
    
        # 2. Find the highest frequency
        max_freq = max(frequencies)
    
        # 3. Find how many tasks have that exact peak frequency
        count_of_max_freq = frequencies.count(max_freq)
    
        # 4. Calculate the formula value
        formula_result = (max_freq - 1) * (n + 1) + count_of_max_freq
    
        # 5. Return the larger of the formula or the raw array length
        return max(len(tasks), formula_result)