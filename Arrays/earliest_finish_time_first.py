class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        answer = float('inf')

        for i in range(len(landStartTime)):

            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = (
                    landStartTime[i] +
                    landDuration[i]
                )

                water_start = max(
                    land_finish,
                    waterStartTime[j]
                )

                answer = min(
                    answer,
                    water_start + waterDuration[j]
                )

                # Water -> Land
                water_finish = (
                    waterStartTime[j] +
                    waterDuration[j]
                )

                land_start = max(
                    water_finish,
                    landStartTime[i]
                )

                answer = min(
                    answer,
                    land_start + landDuration[i]
                )

        return answer


# Test Code
landStartTime = [2,8]
landDuration = [4,1]

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