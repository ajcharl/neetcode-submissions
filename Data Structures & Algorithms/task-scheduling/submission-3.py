class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
    # We use negative numbers because Python only has a min-heap by default
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
    
        time = 0
        # The queue stores pairs of: [remaining_count, available_time]
        cooldown_queue = deque() 
    
     # Keep ticking the clock as long as we have tasks to process
        while max_heap or cooldown_queue:
            time += 1
        
        # Pull the most frequent available task from the heap
            if max_heap:
                # It's a negative number, so adding 1 reduces its remaining count
                cnt = heapq.heappop(max_heap) + 1 
            
                # If there are still instances of this task left, put it on the cooldown bench
                if cnt != 0:
                    cooldown_queue.append([cnt, time + n])
                
        # Check if the task at the front of the bench has finished cooling down
            if cooldown_queue and cooldown_queue[0][1] == time:
            # Unbox it and put it back into the pool of available tasks
                ready_task_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_task_cnt)
            
        return time