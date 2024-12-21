class LC151(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_ls = s.split()
        re_word_ls = reversed(word_ls)
        return " ".join(re_word_ls)

    def reverseWords_double_indexes(self, s):
        s = s.strip()
        # double index
        # ref: https://leetcode.cn/problems/reverse-words-in-a-string/solutions/2361551/151-fan-zhuan-zi-fu-chuan-zhong-de-dan-c-yb1r
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            # here i is point to the blank and the s[j + 1] is not included in this string
            res.append(s[i + 1: j + 1])
            while i >= 0 and s[i] == " ":
                i -= 1
                # make j always point to the end of next word
                j = i
        return " ".join(res)

lc = LC151()
print(lc.reverseWords("the sky is blue"))
print(lc.reverseWords_double_indexes("the sky is blue"))
"""
Time Complexity: O(n) where n is the length of the word.
Space Complexity: O(n) to store the reversed string and return.
"""