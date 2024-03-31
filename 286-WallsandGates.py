from queue import Queue
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.row, self.col = len(rooms), len(rooms[0])
        self.q = Queue()
        self.visited = set()
        
        # Add gates position into q
        for i in range(self.row):
            for j in range(self.col):
                if rooms[i][j] == 0:
                    self.q.put((i, j))
                    self.visited.add((i, j))
        
        # BFS
        dist = 0
        while not self.q.empty():
            for _ in range(self.q.qsize()):
                x, y = self.q.get()
                rooms[x][y] = dist
                self.bfs(rooms, x + 1, y)
                self.bfs(rooms, x - 1, y)
                self.bfs(rooms, x, y + 1)
                self.bfs(rooms, x, y - 1)

            dist += 1

    
    def bfs(self, rooms, x, y):
        # return
        if (x < 0 or x == self.row or y < 0 or y == self.col or (x, y) in self.visited or rooms[x][y] == -1):
            return
        
        self.visited.add((x, y))
        self.q.put((x, y))
