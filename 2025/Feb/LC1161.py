from collections import deque
class LC1161:
    def maxLevelSum(self, root) -> int:
        max_level = cur_level = 0
        bfs_queue = deque()
        bfs_queue.append(root)
        max_level_val = float('-inf')
        while bfs_queue:
            cur_level += 1
            cur_level_sum = 0
            for _ in range(len(bfs_queue)):
                cur_node = bfs_queue.popleft()
                cur_level_sum += cur_node.val
                if cur_node.left:
                    bfs_queue.append(cur_node.left)
                if cur_node.right:
                    bfs_queue.append(cur_node.right)
            if cur_level_sum > max_level_val:
                max_level_val = cur_level_sum
                max_level = cur_level
        return max_level
