class LC1448(object):
    def goodNodes(self, root):
        return self.dfs(root, float('-inf'))

    def dfs(self, root, path_max):
        if root is None:
            return 0
        res = 0
        if root.val >= path_max:
            res += 1
            path_max = root.val
        res += self.dfs(root.left, path_max) + self.dfs(root.right, path_max)
        return res