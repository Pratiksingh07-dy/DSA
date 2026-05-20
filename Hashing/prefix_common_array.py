class Solution:
    def findThePrefixCommonArray(self, A, B):

        seen = set()

        common = 0

        result = []

        for i in range(len(A)):

            if A[i] in seen:
                common += 1

            seen.add(A[i])

            if B[i] in seen:
                common += 1

            seen.add(B[i])

            result.append(common)

        return result


# Test Code
A=[1,3,2,5,7,4]
B=[3,1,7,3,2,4]

obj = Solution()

answer = obj.findThePrefixCommonArray(A,B)

print(answer)


# here i need to check whether a number has already
# appeared in both arrays quickly.
#
# My thinking:
# 1. Traverse both arrays together
# 2. Store seen numbers in a set
# 3. If current number already exists in set,
#    increase common count
# 4. Store current number in set
# 5. Add current common count to result array