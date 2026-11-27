class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = True

        while n >= stones:
            n -= stones
            stones -= 1
            alice_turn = not alice_turn

        return not alice_turn


sol = Solution()

print(sol.canAliceWin(12))  # True
print(sol.canAliceWin(1))   # False
print(sol.canAliceWin(20))  # False
print(sol.canAliceWin(55))  # True