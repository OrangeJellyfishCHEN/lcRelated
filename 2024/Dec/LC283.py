class LC283(object):
    def moveZeros(self, nums):
        n = len(nums)
        # make sure the left part to l pointer is always non-zero
        l = r = 0
        while r < n:
            # when the nums[l] is zero, r need to find the first non-zero number to swap
            # else, l and r is at the same place, they swapped themselves
            # 如果数组没有0，那么快慢指针始终指向同一个位置，每个位置自己和自己交换；如果数组有0，快指针先走一步，此时慢指针对应的就是0，所以要交换。
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

lc = LC283()
nums = [0, 0, 2]
lc.moveZeros(nums)
print(nums)

