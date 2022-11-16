class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        return self.bfs(maze, start, destination)

    def bfs(self, maze, start, destination) -> bool:
        Row, Col = len(maze), len(maze[0])
        visited = [[False for _ in range(Col)] for _ in range(Row)] 
        Q = [(start[0], start[1])]         
        visited[start[0]][start[1]] = True
        while Q:
            r, c = Q.pop(0)
            if [r,c] == destination:   
                return True
            for dr,dc in ((0,1), (1,0), (0,-1), (-1,0)):
                nr = r + dr
                nc = c + dc
                while 0<= nr <Row and 0<= nc <Col and maze[nr][nc]==0: 
                    nr += dr
                    nc += dc
                nr -= dr      
                nc -= dc       
                if visited[nr][nc] == False: 
                    visited[nr][nc] = True
                    Q.append((nr, nc))
        return False


def main():
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    start = [0, 4]
    destination = [4, 4]
    print(Solution().hasPath(maze, start, destination))


if __name__ == "__main__":
    main()
