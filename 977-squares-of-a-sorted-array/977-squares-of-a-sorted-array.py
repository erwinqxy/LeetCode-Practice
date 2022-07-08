class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      squared = list(map(lambda x:x**2, nums))
      squared.sort()
      return squared
    
    #interesting info: 
    # Time Complexity: O(nlogn) 
    #list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(n)
    #the Arrays.sort() in Java is a variant of quicksort algorithm whose space complexity is O(logN).