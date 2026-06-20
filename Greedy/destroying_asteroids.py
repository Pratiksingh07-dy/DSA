# 2126 Destorying Asteroids

class Solution:
    def asteroidsDestroyed(self, mass, asteroids):

        asteroids.sort()

        for asteroid in asteroids:

            if mass < asteroid:
                return False

            mass += asteroid

        return True


# Test Code
mass = 10
asteroids = [3,13,19,5,21]

obj = Solution()

answer = obj.asteroidsDestroyed(
    mass,
    asteroids
)

print(answer)



# Pattern Used: Greedy
#
# Why:
# Always destroy the smallest
# asteroid first to gain mass.
#
# My thinking:
# 1. Sort asteroids
# 2. Destroy smallest first
# 3. Increase planet mass
# 4. If any asteroid is bigger
#    than current mass, return False
# 5. Otherwise return True
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)