class LC79(object):
    def maxOperations(self, nums, k):
        ans = 0
        nums_hash = {}
        for num in nums:
            if k - num in nums_hash and nums_hash[k - num] > 0:
                nums_hash[k - num] -= 1
                ans += 1
            else:
                if num not in nums_hash:
                    nums_hash[num] = 0
                nums_hash[num] += 1
        return ans
