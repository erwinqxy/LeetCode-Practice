class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      triangle = []
      
      for i in range (0, numRows):
        curr = [1 for x in range(i+1)]
        if (i == 0 or i == 1):
          triangle.append(curr)
        else:
          for j in range (1, len(curr) - 1):
            curr[j] = triangle[-1][j-1] + triangle[-1][j]
          triangle.append(curr)
      return triangle