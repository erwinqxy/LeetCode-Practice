class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def memo_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = memo_fib(N-1) + memo_fib(N-2)

            # put result in cache for later reference.
            cache[N] = result
            return result
        
        return memo_fib(N)
        