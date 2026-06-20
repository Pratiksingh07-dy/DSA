# 1871 JUMP GAME VII

from collections import deque


class Solution:
    def canReach(self, s, minJump, maxJump):

        n = len(s)

        queue = deque([0])

        farthest = 0

        while queue:

            current = queue.popleft()

            start = max(
                current + minJump,
                farthest + 1
            )

            end = min(
                current + maxJump,
                n - 1
            )

            for next_pos in range(start,end+1):

                if s[next_pos] == '0':

                    if next_pos == n-1:
                        return True

                    queue.append(next_pos)

            farthest = end

        return n==1


# Test Code
s="011010"
minJump=2
maxJump=3

obj=Solution()

answer=obj.canReach(
    s,
    minJump,
    maxJump
)

print("Can Reach:",answer)


#
# Pattern Used: BFS 
#
# Why:
# Need shortest exploration but
# checking all jumps repeatedly
# becomes slow.
#
# My thinking:
# 1. Start BFS from index 0
# 2. Explore valid jump range
# 3. Visit only '0'
# 4. Avoid rechecking positions
# 5. Return True if last index reached
#
# Time Complexity: O(n)
