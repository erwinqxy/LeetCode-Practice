/**
Break the problem down: 
now we have x^(n/2)
if n is even to get x^(n) we can just x^(n/2) * x^(n/2)
if n is odd to get x^(n) we can just x^(n/2) * x^(n/2) * x 
**/
class Solution {
    private double fastPowHelper(double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        double half = fastPowHelper(x, n / 2);
        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        return fastPowHelper(x, N);
    }
};