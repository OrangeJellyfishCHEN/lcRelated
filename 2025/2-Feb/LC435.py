class LC435:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        ans = 1
        n = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        return n - ans