def shortestBeautifulSubstring(s, k):
    left = 0
    ones = 0
    ans = ""

    for right in range(len(s)):
        if s[right] == '1':
            ones += 1

        while ones > k:
            if s[left] == '1':
                ones -= 1
            left += 1

        if ones == k:
            while s[left] == '0':
                left += 1

            current = s[left:right + 1]

            if ans == "" or len(current) < len(ans):
                ans = current
            elif len(current) == len(ans) and current < ans:
                ans = current

    return ans


s = "100011001"
k = 3

print(shortestBeautifulSubstring(s, k))