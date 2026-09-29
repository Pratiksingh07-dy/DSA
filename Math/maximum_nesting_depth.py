class Solution:
    def maxDepth(self, s):
        depth = 0
        answer = 0

        for ch in s:
            if ch == '(':
                depth += 1
                answer = max(answer, depth)
            elif ch == ')':
                depth -= 1

        return answer


if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"

    solution = Solution()
    print(solution.maxDepth(s))