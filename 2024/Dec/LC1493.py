class LC1493(object):
    def longestSubarray(self, nums):
        l = 0
        max_length = 0
        count_zero = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
            while count_zero > 1:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            max_length = max(max_length, r - l)
        return max_length