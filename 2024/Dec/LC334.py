class LC334(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        first = 0
        second = float('inf')
        for i in range(len(nums)):
            cur = nums[i]
            if cur > second:
                return True
            elif first < cur <= second:
                second = cur
            else:
                first = cur
        return False

