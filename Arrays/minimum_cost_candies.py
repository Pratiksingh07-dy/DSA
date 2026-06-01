# 2144. Minimum Cost of Buying Candies With Discount

class Solution:
    def minimumCost(self, cost):

        cost.sort(reverse=True)

        total = 0

        for i in range(len(cost)):

            if i % 3 != 2:
                total += cost[i]

        return total


# Test Code
cost = [6,5,7,9,2,2]

obj = Solution()

answer = obj.minimumCost(cost)

print(answer)



# Pattern Used: Sorting
#
# Why:
# Every 3rd candy can be free.
#
# My thinking:
# 1. Sort in descending order
# 2. Take most expensive candies first
# 3. Every 3rd candy becomes free
# 4. Add only paid candies
#
# Time Complexity: O(n log n)
# -----------------------------