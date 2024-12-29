class LC27(object):
    def removeElement(self, nums, val):
        # fast is read index and slow is the write index
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
