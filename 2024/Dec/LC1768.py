class LC1768(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        res = ""
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
            i += 1
        return res


lc = LC1768()
print(lc.mergeAlternately("abc", "pqr"))
print(lc.mergeAlternately("ab", "pqrs"))

"""
Time complexity: O(n + m) -> need to iterate every char in each word
Space Complexity: O(n + m) -> to store the result string and return
"""
