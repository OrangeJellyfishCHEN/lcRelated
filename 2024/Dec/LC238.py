class LC238(object):
    def productExpectSelf(self, nums):
        # method: prefix twice.
        n = len(nums)
        ans = [1] * n
        j = 1
        for i in range(1, n + 1):
            ans *= j
            j *= nums[n - 1]
        j = 1
        for i in range(n, 0, -1):
            ans *= j
            j *= nums[n - 1]
        return ans
