class LC2215(object):
    def findDefference(self, nums1, nums2):
        res = [[], []]
        for num in nums1:
            if num not in set(nums2):
                res[0].append(num)
        for num in nums2:
            if num not in set(nums1):
                res[1].append(num)
        return res
