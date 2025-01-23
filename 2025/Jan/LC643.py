class LC643(object):
    def findMaxAverage(self, nums, k):
        max_total = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            max_total = max(max_total, total)
        return max_total / k