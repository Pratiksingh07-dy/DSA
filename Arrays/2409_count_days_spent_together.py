
class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        months = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

        def to_days(date):
            month, day = map(int, date.split("-"))
            return sum(months[:month - 1]) + day

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        return max(0, end - start + 1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.countDaysTogether("08-15", "08-18", "08-16", "08-19"))  # 3
    print(sol.countDaysTogether("10-01", "10-31", "11-01", "12-31"))  # 0
