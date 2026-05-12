
class Solution:
    def longestCommonPrefix(self, strs):

        prefix = strs[0]

        for s in strs[1:]:

            while not s.startswith(prefix):

                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


# Test Code
strs = ["flower", "flow", "flight"]

obj = Solution()

answer = obj.longestCommonPrefix(strs)

print("Longest Common Prefix:", answer)