class LC1431(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_c = max(candies)
        res = []
        for candy in candies:
            res.append(candy + extraCandies >= max_c)
        return res
        # shorter version
        # return [c + extraCandies >= max_c for c in candies]