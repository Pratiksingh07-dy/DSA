from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Find the next strictly greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Step 2: Build prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Cost of raising all elements after i
        # up to (but not including) nxt[i] to nums[i]
        base_cost = [0] * n

        for i in range(n):
            length = nxt[i] - i - 1
            total = prefix[nxt[i]] - prefix[i + 1]
            base_cost[i] = nums[i] * length - total

        # Step 3: Binary lifting tables
        LOG = n.bit_length()

        up = [nxt]
        cost = [base_cost]

        for j in range(1, LOG):
            prev_up = up[-1]
            prev_cost = cost[-1]

            curr_up = [n] * n
            curr_cost = [0] * n

            for i in range(n):
                mid = prev_up[i]

                if mid < n:
                    curr_up[i] = prev_up[mid]
                    curr_cost[i] = prev_cost[i] + prev_cost[mid]
                else:
                    curr_cost[i] = prev_cost[i]

            up.append(curr_up)
            cost.append(curr_cost)

        # Step 4: Find the maximum valid endpoint for each start
        answer = 0

        for left in range(n):
            pos = left
            remaining = k

            # Skip complete segments whenever affordable
            for j in range(LOG - 1, -1, -1):
                segment_cost = cost[j][pos]
                next_pos = up[j][pos]

                if segment_cost <= remaining:
                    remaining -= segment_cost
                    pos = next_pos

                    if pos == n:
                        break

            if pos == n:
                right = n - 1

            else:
                # Binary search inside the current segment
                low = 0
                high = nxt[pos] - pos - 1

                while low < high:
                    mid = (low + high + 1) // 2

                    required = (
                        nums[pos] * mid
                        - (prefix[pos + mid + 1] - prefix[pos + 1])
                    )

                    if required <= remaining:
                        low = mid
                    else:
                        high = mid - 1

                right = pos + low

            answer += right - left + 1

        return answer