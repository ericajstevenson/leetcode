def climbStairs(n):
    if n <= 2: return n
    prev1 = 1
    prev2  = 2
    for i in range(3, n+1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2



print(climbStairs(10))