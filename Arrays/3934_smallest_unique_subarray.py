from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        a = nums + [0]
        m = n + 1

        p = sorted(range(m), key=lambda i: a[i])
        c = [0] * m
        classes = 1

        for i in range(1, m):
            if a[p[i]] != a[p[i - 1]]:
                classes += 1
            c[p[i]] = classes - 1

        length = 1

        while length < m:
            pn = [(x - length) % m for x in p]

            cnt = [0] * classes
            for x in pn:
                cnt[c[x]] += 1

            pos = [0] * classes
            for i in range(1, classes):
                pos[i] = pos[i - 1] + cnt[i - 1]

            new_p = [0] * m

            for x in pn:
                cl = c[x]
                new_p[pos[cl]] = x
                pos[cl] += 1

            p = new_p

            new_c = [0] * m
            new_classes = 1

            for i in range(1, m):
                cur = (c[p[i]], c[(p[i] + length) % m])
                prev = (c[p[i - 1]], c[(p[i - 1] + length) % m])

                if cur != prev:
                    new_classes += 1

                new_c[p[i]] = new_classes - 1

            c = new_c
            classes = new_classes
            length *= 2

        sa = [x for x in p if x != n]

        rank = [0] * n
        for i, start in enumerate(sa):
            rank[start] = i

        lcp = [0] * n
        k = 0

        for i in range(n):
            r = rank[i]

            if r == 0:
                k = 0
                continue

            j = sa[r - 1]

            while (i + k < n and j + k < n
                   and nums[i + k] == nums[j + k]):
                k += 1

            lcp[r] = k

            if k > 0:
                k -= 1

        answer = n

        for r in range(n):
            start = sa[r]

            common = max(
                lcp[r],
                lcp[r + 1] if r + 1 < n else 0
            )

            needed = common + 1

            if needed <= n - start:
                answer = min(answer, needed)

        return answer