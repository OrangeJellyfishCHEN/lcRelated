class LC977(object):
    def sortedSquares(self, nums):
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        i = len(nums) - 1
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i -= 1
        return res