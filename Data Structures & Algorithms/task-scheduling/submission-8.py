class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        waiting = deque()

        while max_heap or waiting:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    waiting.append([count, time + n])
            
            if waiting and waiting[0][1] == time:
                ready_task, _ = waiting.popleft()
                heapq.heappush(max_heap, ready_task)
        return time

        