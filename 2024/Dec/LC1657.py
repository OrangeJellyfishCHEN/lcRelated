from collections import Counter


class LC1657(object):
    def closeStrings(self, word1, word2):
        w1_countval = Counter(word1).values()
        w2_countval = Counter(word2).values()
        return set(word1) == set(word2) and sorted(w2_countval) == sorted(w1_countval)
