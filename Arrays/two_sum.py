class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i


# Test Code
nums = [2, 7, 11, 15]
target = 9

obj = Solution()
answer = obj.twoSum(nums, target)

print("Output:", answer)