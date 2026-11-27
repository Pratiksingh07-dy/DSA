from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        min_price = min(price for factor, price in items)

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            value = 1 + free[i]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        answer = 0

        for spent in range(budget + 1):
            extra = (budget - spent) // min_price
            answer = max(answer, dp[spent] + extra)

        return answer