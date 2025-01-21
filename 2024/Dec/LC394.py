class LC394(object):
    def decodeString(self, s):
        s_stack = []
        for ch in s:
            if "0" <= ch <= "9" or "a" <= ch <= "z" or ch == "[":
                s_stack.append(ch)
            else:
                temp = ""
                while s_stack and s_stack[-1] != "[":
                    temp += s_stack.pop()
                temp = temp[::-1]
                s_stack.pop()
                time = ""
                while s_stack and "0" <= s_stack[-1] <= "9":
                    time += s_stack.pop()
                time = int(time[::-1])
                ret = time * temp
                for ch in ret:
                    s_stack.append(ch)
        return "".join(s_stack)