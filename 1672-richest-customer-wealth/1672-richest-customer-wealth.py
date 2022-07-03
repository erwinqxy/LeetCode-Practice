class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
      sumAccounts = list(map(lambda x: sum(x), accounts))
      return max(sumAccounts)