class Solution:

    def shiftGrid(
        self,
        grid,
        k
    ):

        m = len(grid)

        n = len(grid[0])

        total = m * n

        # Remove unnecessary
        # full rotations

        k %= total


        # Convert 2D grid
        # into 1D array

        flat = []

        for row in grid:

            flat.extend(row)


        # Shift array
        # to the right by k

        if k > 0:

            flat = (

                flat[-k:]

                +

                flat[:-k]

            )


        # Convert 1D array
        # back into 2D grid

        answer = []

        for i in range(

            0,

            total,

            n

        ):

            answer.append(

                flat[i:i + n]

            )

        return answer


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Simulation
#
#
# My Thinking:
#
# 1. Convert 2D grid
#    into a 1D array.
#
# 2. Shift the array
#    right by k places.
#
# 3. Convert it back
#    into the original
#    grid dimensions.
#
#
# Time Complexity:
#
# O(m * n)
#
#
# Space Complexity:
#
# O(m * n)
# ----------------------------------


grid = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

k = 1


obj = Solution()

result = obj.shiftGrid(

    grid,

    k

)

print(result)


# Output:
#
# [[9, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]