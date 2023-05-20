class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = 1
        summ = 0 
        while n > 0:
            summ += n%10
            prod *= n%10
            n = n // 10
        return prod - summ
    
        