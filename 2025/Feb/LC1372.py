class LC1372:
    def longestZigZag(self, root) -> int:
        max_ans = 0
        def dfs(node, direction, length):
            if node is None:
                return
            nonlocal max_ans
            max_ans = max(max_ans, length)
            # left
            if direction == 0:
                dfs(node.left, 1, length + 1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.left, 1, 1)
                dfs(node.right, 0, length + 1)
        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return max_ans