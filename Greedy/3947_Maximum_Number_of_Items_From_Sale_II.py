from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Count how many items have each factor
        max_factor = max(factor for factor, price in items)

        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Count all eligible free items for each factor
        gifts = [0] * (max_factor + 1)

        for factor in range(1, max_factor + 1):
            for multiple in range(factor, max_factor + 1, factor):
                gifts[factor] += freq[multiple]

            # Exclude the item itself
            gifts[factor] -= freq[factor] > 0

        # Step 3: Find the cheapest item
        cheapest = min(price for factor, price in items)

        # Step 4: Group profitable double-item purchases by price
        deals = {}

        for factor, price in items:
            extra = gifts[factor]

            if extra > 0 and price < 2 * cheapest:
                deals[price] = deals.get(price, 0) + extra

        # Step 5: Purchase the most profitable deals first
        total = 0

        for price in sorted(deals):
            count = min(deals[price], budget // price)

            total += count * 2
            budget -= count * price

            if budget == 0:
                return total

        # Step 6: Spend remaining budget on the cheapest item
        total += budget // cheapest

        return total
