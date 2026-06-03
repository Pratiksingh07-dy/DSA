from bisect import bisect_right


class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def build(starts, durations):

            rides = sorted(zip(starts, durations))

            s = [x for x, _ in rides]

            prefix_min_duration = [0] * len(rides)

            prefix_min_duration[0] = rides[0][1]

            for i in range(1, len(rides)):

                prefix_min_duration[i] = min(
                    prefix_min_duration[i - 1],
                    rides[i][1]
                )

            suffix_min_finish = [0] * len(rides)

            suffix_min_finish[-1] = (
                rides[-1][0] +
                rides[-1][1]
            )

            for i in range(
                len(rides) - 2,
                -1,
                -1
            ):

                suffix_min_finish[i] = min(
                    suffix_min_finish[i + 1],
                    rides[i][0] + rides[i][1]
                )

            return (
                s,
                prefix_min_duration,
                suffix_min_finish
            )

        water_s, water_pref, water_suff = build(
            waterStartTime,
            waterDuration
        )

        land_s, land_pref, land_suff = build(
            landStartTime,
            landDuration
        )

        answer = float("inf")

        # Land -> Water
        for ls, ld in zip(
            landStartTime,
            landDuration
        ):

            finish_land = ls + ld

            idx = bisect_right(
                water_s,
                finish_land
            ) - 1

            if idx >= 0:

                answer = min(
                    answer,
                    finish_land +
                    water_pref[idx]
                )

            if idx + 1 < len(water_suff):

                answer = min(
                    answer,
                    water_suff[idx + 1]
                )

        # Water -> Land
        for ws, wd in zip(
            waterStartTime,
            waterDuration
        ):

            finish_water = ws + wd

            idx = bisect_right(
                land_s,
                finish_water
            ) - 1

            if idx >= 0:

                answer = min(
                    answer,
                    finish_water +
                    land_pref[idx]
                )

            if idx + 1 < len(land_suff):

                answer = min(
                    answer,
                    land_suff[idx + 1]
                )

        return answer


# Test Code

landStartTime = [2, 8]
landDuration = [4, 1]

waterStartTime = [6]
waterDuration = [3]

obj = Solution()

answer = obj.earliestFinishTime(
    landStartTime,
    landDuration,
    waterStartTime,
    waterDuration
)

print(answer)


# Pattern Used: Sorting + Binary Search
#
# Why:
# n and m can be 50000,
# so checking every pair causes TLE.
#
# My thinking:
# 1. Sort rides by opening time
# 2. Build prefix minimum duration
# 3. Build suffix minimum finish time
# 4. Use binary search to find
#    rides available at current time
# 5. Calculate earliest possible finish
#
# Time Complexity:
# O((n+m) log(n+m))
#
# Space Complexity:
# O(n+m)
