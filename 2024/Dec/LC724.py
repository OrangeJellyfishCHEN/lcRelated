class LC724(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if 2 * prefix == total - nums[i]:
                return i
            prefix += nums[i]
        return -1