class LC2390(object):
    def removeStars(self, s):
        str_stack = []
        for ch in s:
            if ch == "*" and len(str_stack) > 0:
                str_stack.pop()
            else:
                str_stack.append(ch)
        return "".join(str_stack)