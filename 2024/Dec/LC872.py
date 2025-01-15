class LC872(object):
    def leafSimilar(self, root1, root2):
        res1 = []
        res2 = []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return res1 == res2


    def dfs(self, root, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)