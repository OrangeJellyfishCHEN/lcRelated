class LC1071(object):
    def gcdOfStrings(self, str1, str2):
        div_len = self.gcd(len(str1), len(str2))
        div = str1[:div_len]
        if str1 + str2 == str2 + str2:
            return div
        return ""

    def gcd(self, a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a