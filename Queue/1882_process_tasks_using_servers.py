import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            # Release all servers that have finished their tasks.
            while busy and busy[0][0] <= time:
                free_time, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            # If no server is available, wait for the earliest one.
            if not available:
                time = busy[0][0]

                # Release every server that becomes free at this time.
                while busy and busy[0][0] <= time:
                    free_time, weight, server = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server))

            # Assign the task to the best available server.
            weight, server = heapq.heappop(available)
            ans.append(server)

            # Store its next available time.
            heapq.heappush(busy, (time + task, weight, server))

        return ans


if __name__ == "__main__":
    sol = Solution()

    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]

    print(sol.assignTasks(servers, tasks))