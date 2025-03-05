class LC452:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[1])
        right = points[0][1]
        ans = 1
        for i in range(len(points)):
            if points[i][0] > right:
                ans += 1
                right = points[i][1]
        return ans