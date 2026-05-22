class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            # Left half sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            # Right half sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1


# Test Code
nums=[4,5,6,7,0,1,2]
target=0

obj=Solution()

answer=obj.search(nums,target)

print("Index:",answer)



# Pattern Used: Binary Search
#
# Why:
# Sorted array + O(log n)
# but array is rotated.
#
# My thinking:
# 1. Find middle
# 2. Check which side is sorted
# 3. Check if target lies there
# 4. Move left/right
# 5. Repeat
#
# Time Complexity: O(log n)
