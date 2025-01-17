class LC437(object):
    def pathSum(self, root, targetSum):
        if root is None:
            return 0
        ret = self.dfs(root, targetSum)
        ret += self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return ret

    def dfs(self, root, targetSum):
        if root is None:
            return 0
        ret = 0
        if root.val == targetSum:
            ret += 1
        ret += self.dfs(root.left, targetSum - root.val) + self.dfs(root.right, targetSum - root.val)
        return ret