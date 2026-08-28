def lexPalindromicPermutation(s, target):

    n = len(s)

    cnt = [0] * 26

    for ch in s:
        cnt[ord(ch) - 97] += 1

    odd = 0
    middle = ""

    for i in range(26):
        if cnt[i] % 2:
            odd += 1
            middle = chr(i + 97)

    if odd > 1:
        return ""

    half = [x // 2 for x in cnt]
    m = n // 2

    def make_pal(left):
        if n % 2:
            return left + middle + left[::-1]
        return left + left[::-1]

    # First try exact target left half
    rem = half[:]
    left = []
    possible = True

    for i in range(m):
        c = ord(target[i]) - 97

        if rem[c] == 0:
            possible = False
            break

        rem[c] -= 1
        left.append(target[i])

    if possible:
        for c in range(26):
            if rem[c]:
                left.extend([chr(c + 97)] * rem[c])

        candidate = make_pal("".join(left))

        if candidate > target:
            return candidate

    # Try making the left half greater
    for i in range(m - 1, -1, -1):

        rem = half[:]
        left = []
        possible = True

        for j in range(i):
            c = ord(target[j]) - 97

            if rem[c] == 0:
                possible = False
                break

            rem[c] -= 1
            left.append(target[j])

        if not possible:
            continue

        target_char = ord(target[i]) - 97

        for c in range(target_char + 1, 26):

            if rem[c] == 0:
                continue

            rem[c] -= 1

            new_left = left + [chr(c + 97)]

            for x in range(26):
                if rem[x]:
                    new_left.extend([chr(x + 97)] * rem[x])

            candidate = make_pal("".join(new_left))

            if candidate > target:
                return candidate

            rem[c] += 1

    return ""


# Input
s = input().strip()
target = input().strip()

# Output
print(lexPalindromicPermutation(s, target))