class LC1004(object):
    def longestOnes(self, nums, k):
        l = 0
        count_zero = 0
        max_length = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
            while count_zero > k:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
