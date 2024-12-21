class LC345(object):
    def reverseVowels(self, s):
        vows = set('aeiouAEIOU')
        chars = list(s)
        # two pointers to find the reverse
        l = 0
        r = len(s) - 1
        while l < r:
            while l < len(s) and l not in vows:
                l += 1
            while r > 0 and r not in vows:
                r -= 1
            # double pointer meet then break
            if l >= r:
                break
            chars[l], chars[r] = chars[r], chars[l]
            # both move to the next char
            l += 1
            r -= 1
        return "".join(chars)


