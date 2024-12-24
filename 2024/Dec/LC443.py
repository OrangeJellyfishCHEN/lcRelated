class LC443(object):
    def compress(self, chars):
        n = len(chars)
        # number of current same chars
        cnt = 1
        # pointer point to position write in
        j = 0
        for i in range(n):
            if i == n - 1 or chars[i] != chars[i + 1]:
                chars[j] = chars[i]
                j += 1
                # if cnt > 1 we need to add number
                if cnt > 1:
                    for k in str(cnt):
                        chars[j] = k
                        j += 1
                # initialize cnt
                cnt = 1
            else:
                cnt += 1
        return j


lc = LC443()
chars = ["a","a","b","b","c","c","c"]
l = lc.compress(chars)
print(chars[:l])
