from typing import List


class LC3229:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        l = len(nums)
        temp = []
        for i in range(l):
            temp.append(nums[i] - target[i])
        res = abs(temp[0])
        for j in range(1, l):
            cur = temp[j]
            prev = temp[j - 1]
            print([cur,prev])
            if cur * prev <= 0:
                res += abs(cur)
                continue
            gap = abs(cur) - abs(prev)
            if gap > 0:
                res += gap
        return res


print(LC3229().minimumOperations([1,3,2], [2,1,4]))
print(LC3229().minimumOperations([3,5,1,2], [4,6,2,4]))

