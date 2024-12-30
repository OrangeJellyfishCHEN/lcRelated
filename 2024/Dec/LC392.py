class LC392(object):
    def isSubsequence(self, s, t):
        index_t = index_s = 0
        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
        return index_s == len(s)