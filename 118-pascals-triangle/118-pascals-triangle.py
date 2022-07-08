class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      
      pascalTri = [] 
      for i in range(1, numRows+1): 
        if (i == 1):
          pascalTri += [[1],]
        elif (i == 2):
          pascalTri += [[1,1],]
        else:
          prevArray = pascalTri[i-2]
          new = [1,]
          for i in range (len(prevArray)-1):
            new += [(prevArray[i] + prevArray[i+1]),]
          new += [1,]
          pascalTri += [new,] 
      return pascalTri
              