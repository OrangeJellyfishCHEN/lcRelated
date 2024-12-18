class LC151(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_ls = s.split()
        re_word_ls = reversed(word_ls)
        return " ".join(re_word_ls)

    def reverseWords(self, s):
        #TODO: dont use split an use double indexes
        return None


lc = LC151()
print(lc.reverseWords("the sky is blue"))

"""
Time Complexity: O(n) where n is the length of the word.
Space Complexity: O(n) to store the reversed string and return.
"""