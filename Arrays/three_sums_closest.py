class Solution:
    def getCommon(self, nums1, nums2):

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                return nums1[i]

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return -1


# Test Code
nums1 = [1,2,3]
nums2 = [2,4]

obj = Solution()

answer = obj.getCommon(nums1, nums2)

print("Minimum Common:",answer)