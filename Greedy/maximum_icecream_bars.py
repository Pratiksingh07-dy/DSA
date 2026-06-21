class Solution:

    def maxIceCream(self, costs, coins):

        maximum_cost = max(costs)

        frequency = [0] * (maximum_cost + 1)

        for cost in costs:

            frequency[cost] += 1

        answer = 0

        for cost in range(1, maximum_cost + 1):

            if frequency[cost] == 0:
                continue

            can_buy = min(
                frequency[cost],
                coins // cost
            )

            answer += can_buy

            coins -= can_buy * cost

        return answer


# Test

costs = [1,3,2,4,1]
coins = 7

obj = Solution()

print(
    obj.maxIceCream(
        costs,
        coins
    )
)

# Output:
# 4


# -----------------------------
# Pattern Used:
# Greedy + Counting Sort
#
# Why:
# Need maximum number of
# ice creams.
#
# My thinking:
# 1. Buy cheapest ice creams first.
# 2. Count frequency of each cost.
# 3. Process costs from small
#    to large.
# 4. Buy as many as possible.
#
# Example:
#
# costs = [1,3,2,4,1]
# coins = 7
#
# Sorted costs:
# [1,1,2,3,4]
#
# Buy:
# 1 + 1 + 2 + 3 = 7
#
# Total bought = 4
#
# Time Complexity:
# O(n + max(cost))
#
# Space Complexity:
# O(max(cost))
# -----------------------------