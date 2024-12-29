# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class LC374(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            middle = left + (right - left) // 2
            if guess(middle) <= 0:
                right = middle
            elif guess(middle) == 1:
                left = middle + 1
        return left