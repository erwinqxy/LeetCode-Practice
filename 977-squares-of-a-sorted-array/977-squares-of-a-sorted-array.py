class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      squared = list(map(lambda x:x**2, nums))
      squared.sort()
      return squared