class LC547:
    def findCircleNum(self, isConnected) -> int:
        def dfs(city: int):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
