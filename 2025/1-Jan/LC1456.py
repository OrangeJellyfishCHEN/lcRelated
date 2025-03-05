class LC1456(object):
    def maxVowels(self, s, k):
        set_vow = set("aeiou")
        max_vow = 0
        for i in range(k):
            if s[i] in set_vow:
                max_vow += 1
        cur_vow = max_vow
        for i in range(k, len(s)):
            if s[i] in set_vow:
                cur_vow += 1
            if s[i - k] in set_vow:
                cur_vow -= 1
            max_vow = max(max_vow, cur_vow)
        return max_vow