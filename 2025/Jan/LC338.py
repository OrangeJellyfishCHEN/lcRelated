class LC338(object):
    def countBits(self, n: int):
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        return res


    def countOnes(self, n: int):
        ones = 0
        while n > 0:
            n &= n - 1
            ones += 1
        return ones