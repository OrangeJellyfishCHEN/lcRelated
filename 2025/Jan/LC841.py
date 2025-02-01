class LC841:
    def canVisitAllRooms(self, rooms):
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for room_neighbour in rooms[x]:
                if room_neighbour not in vis:
                    dfs(room_neighbour)
        num = 0
        vis = set()
        dfs(0)
        return num == len(rooms)
