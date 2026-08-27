def lexGreaterPermutation(s, target):
    cnt = [0] * 26

    for ch in s:
        cnt[ord(ch) - ord('a')] += 1

    n = len(s)

    for i in range(n - 1, -1, -1):
        remaining = cnt[:]

        possible = True

        for j in range(i):
            x = ord(target[j]) - ord('a')

            if remaining[x] == 0:
                possible = False
                break

            remaining[x] -= 1

        if not possible:
            continue

        x = ord(target[i]) - ord('a')

        for c in range(x + 1, 26):
            if remaining[c] > 0:
                remaining[c] -= 1

                ans = target[:i] + chr(c + ord('a'))

                for d in range(26):
                    ans += chr(d + ord('a')) * remaining[d]

                return ans

    return ""


s = "abc"
target = "bba"

print(lexGreaterPermutation(s, target))