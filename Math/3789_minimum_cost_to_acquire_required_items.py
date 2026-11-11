class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(need1, need2)

        # Buy type 3 items for the common requirement
        total = both * min(costBoth, cost1 + cost2)

        # Buy remaining individual requirements
        total += (need1 - both) * min(cost1, costBoth)
        total += (need2 - both) * min(cost2, costBoth)

        return total