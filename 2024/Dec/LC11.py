class LC11(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = 0
        # cause l == r is not possible to structure an area
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            #<Greedy> the key point is, only move the pointer with smaller height could get bigger area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
