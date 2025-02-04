import collections


class LC649(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"
