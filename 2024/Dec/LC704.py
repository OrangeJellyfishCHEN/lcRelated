class LC704(object):
    # approach one: possible target field is [left,right]
    def binarySearchOne(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

    # approach two: possible target field is in [left, right)
    def binarySearchTwo(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) / 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
