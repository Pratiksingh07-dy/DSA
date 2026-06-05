class Solution:
    def lengthOfLongestSubstring(self, s):

        seen = set()

        left = 0

        longest = 0

        for right in range(len(s)):

            while s[right] in seen:

                seen.remove(s[left])

                left += 1

            seen.add(s[right])

            longest = max(
                longest,
                right - left + 1
            )

        return longest


# Test Code

s = "abcabcbb"

obj = Solution()

answer = obj.lengthOfLongestSubstring(s)

print(answer)


# -----------------------------
# Pattern Used: Sliding Window
#
# Why:
# Need longest substring
# without repeating characters.
#
# My thinking:
# 1. Use two pointers
#    (left and right)
# 2. Expand window using right
# 3. If duplicate found,
#    shrink window from left
# 4. Track maximum length
# 5. Return answer
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------