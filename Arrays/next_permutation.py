class Solution:
    def nextPermutation(self, nums):

        i = len(nums)-2

        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i>=0:

            j=len(nums)-1

            while nums[j]<=nums[i]:
                j-=1

            nums[i],nums[j]=nums[j],nums[i]

        left=i+1
        right=len(nums)-1

        while left<right:

            nums[left],nums[right]=nums[right],nums[left]

            left+=1
            right-=1


# Test Code
nums=[1,2,3]

obj=Solution()

obj.nextPermutation(nums)

print(nums)

# #31 Next permutation

# -----------------------------
# Pattern Used: Array Manipulation
#
# Why:
# Need next greater arrangement
# without generating all permutations.
#
# My thinking:
# 1. Move from right side
# 2. Find where order breaks
# 3. Find next larger element
# 4. Swap
# 5. Reverse remaining part
#
# Time Complexity: O(n)
# -----------------------------