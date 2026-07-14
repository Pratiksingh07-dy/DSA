class Solution:

    def rotate(
        self,
        matrix
    ):

        n = len(matrix)

        # Step 1 : Transpose

        for i in range(n):

            for j in range(

                i + 1,

                n

            ):

                matrix[i][j], matrix[j][i] = (

                    matrix[j][i],

                    matrix[i][j]

                )

        # Step 2 : Reverse every row

        for row in matrix:

            row.reverse()


# ----------------------------------
# Pattern Used:
#
# Matrix
#
# +
#
# In-place Manipulation
#
#
# Why:
#
# A 90° clockwise
# rotation can be
# achieved by:
#
# 1. Transpose
#
# 2. Reverse each row
#
#
# My Thinking:
#
# 1. Swap rows with
#    columns.
#
# 2. Reverse every row.
#
# 3. Matrix becomes
#    rotated by 90°.
#
#
# Time Complexity:
#
# O(n²)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


matrix = [

    [1,2,3],

    [4,5,6],

    [7,8,9]

]

obj = Solution()

obj.rotate(

    matrix

)

print(

    matrix

)

# Output:
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]