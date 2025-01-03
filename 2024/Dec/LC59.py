class LC59(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        startx = starty = 0
        count = 1
        loop = mid = n // 2
        for offset in range(1, loop + 1):
            # from left to right
            for i in range(starty, n - offset):
                matrix[startx][i] = count
                count += 1
            # from up to down
            for i in range(startx, n - offset):
                matrix[i][n - offset] = count
                count += 1
            # from right to left
            for i in range(n - offset, starty, -1):
                matrix[n - offset][i] = count
                count += 1
            # from down to up
            for i in range(n - offset, startx, -1):
                matrix[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 != 0:
            matrix[mid][mid] = count
        return matrix