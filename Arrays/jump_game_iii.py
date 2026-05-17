class Solution:
    def canReach(self, arr, start):

        visited = set()

        queue = [start]

        while queue:

            current = queue.pop(0)

            if arr[current] == 0:
                return True

            if current in visited:
                continue

            visited.add(current)

            forward = current + arr[current]
            backward = current - arr[current]

            if forward < len(arr):
                queue.append(forward)

            if backward >= 0:
                queue.append(backward)

        return False


# Test Code
arr = [4,2,3,0,3,1,2]
start = 5

obj = Solution()

answer = obj.canReach(arr,start)

print("Can Reach Zero:", answer)