class Solution:
    def searchRange(self, nums, target):

        def findFirst():

            left = 0
            right = len(nums)-1

            first = -1

            while left <= right:

                mid = (left + right)//2

                if nums[mid] == target:

                    first = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return first


        def findLast():

            left = 0
            right = len(nums)-1

            last = -1

            while left <= right:

                mid = (left + right)//2

                if nums[mid] == target:

                    last = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return last


        return [findFirst(), findLast()]


# Test Code
nums=[5,7,7,8,8,10]
target=8

obj=Solution()

answer=obj.searchRange(nums,target)

print(answer)



# Pattern Used: Binary Search
#
# Why:
# Sorted array + O(log n)
#
# My thinking:
# 1. Find first occurrence
# 2. Find last occurrence
# 3. Use binary search twice
# 4. Return both indices
#
#34. Find First and Last Position of Element in Sorted Array
