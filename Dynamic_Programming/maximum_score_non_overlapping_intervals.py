import bisect
import functools
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class T:
    weight: int
    selected: tuple[int, ...]

    def __iter__(self):
        yield self.weight
        yield self.selected


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        intervals = sorted(
            (*interval, i) for i, interval in enumerate(intervals)
        )

        @functools.lru_cache(None)
        def dp(i: int, quota: int) -> T:
            if i == len(intervals) or quota == 0:
                return T(0, ())

            skip = dp(i + 1, quota)

            _, r, weight, originalIndex = intervals[i]

            j = bisect.bisect_right(intervals, (r, math.inf))

            nextRes = dp(j, quota - 1)

            pick = T(
                weight + nextRes.weight,
                tuple(sorted((originalIndex, *nextRes.selected)))
            )

            if (pick.weight > skip.weight or
                    (pick.weight == skip.weight and
                     pick.selected < skip.selected)):
                return pick

            return skip

        return list(dp(0, 4))


if __name__ == "__main__":
    solution = Solution()

    intervals = [
        [1, 3, 2],
        [4, 5, 2],
        [1, 5, 5],
        [6, 9, 3],
        [6, 7, 1],
        [8, 9, 1]
    ]

    print(solution.maximumWeight(intervals))