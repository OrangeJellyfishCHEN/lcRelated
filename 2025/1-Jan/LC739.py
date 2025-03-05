class LC739(object):
    def dailyTemperature(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cur_temperature = temperatures[i]
            while stack and cur_temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans