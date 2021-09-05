import sys


class Solution:
    def __init__(self) -> None:
        self.row = [-1, 0, 1, 0]
        self.col = [0, -1, 0, 1]

    def isSafe(self, arr, visited, row, col):
        return 0 <= row < len(arr) and 0 <= col < len(arr[0]) and not(arr[row][col] == 0 or visited[row][col])

    def shortestPath(self, arr, visited, i, j, dest, min_dist=sys.maxsize, dist=0):
        if (i, j) == dest:
            min_dist = min(min_dist, dist)
            return min_dist

        visited[i][j] = 1

        for m in range(4):
            if self.isSafe(arr, visited, i+self.row[m], j+self.col[m]):
                min_dist = self.shortestPath(
                    arr, visited, i + self.row[m], j+self.col[m], dest, min_dist, dist+1)

        visited[i][j] = 0

        return min_dist


if __name__ == "__main__":
    arr = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    source_x, source_y = (0, 0)
    dest_x, dest_y = (7, 5)

    if not arr or len(arr) == 0 or arr[source_x][source_y] == 0 or arr[dest_x][dest_y] == 0:
        print(-1)
    else:
        visited = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
        obj = Solution()
        min_dist = obj.shortestPath(
            arr, visited, source_x, source_y, (dest_x, dest_y))
        if min_dist == sys.maxsize:
            print(-1)
        else:
            print(min_dist)
