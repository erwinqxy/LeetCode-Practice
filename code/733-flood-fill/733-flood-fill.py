class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      # can use a stack to push things to fill
        R, C = len(image), len(image[0])
        currColor = image[sr][sc]
        if currColor == color: return image
        def dfs(r, c):
            if image[r][c] == currColor:
                image[r][c] = color
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image