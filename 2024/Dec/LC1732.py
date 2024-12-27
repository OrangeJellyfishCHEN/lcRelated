class LC1732(object):
    def largestAltitude(self, gain):
        total, max_val = 0
        for g in gain:
            total += g
            max_val = max(max_val, total)
        return max_val