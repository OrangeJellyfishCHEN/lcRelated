class LC209(object):
    def minSubArrayLen(self, target, nums):
        result = float('inf')
        # sliding window left and right bound and sum of values in the window
        l = r = window_sum = 0
        while r < len(nums):
            window_sum += nums[r]
            # minimize the left boundary
            while window_sum >= target:
                # update result then calculate the new window sum for next iteration
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1
            r += 1
        return result if result != float('inf') else 0