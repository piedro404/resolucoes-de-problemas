class Solution:
    def __init__(self) -> None:
        self.stepsMemo = [1, 1]

    def steps(self, n):            
        if len(self.stepsMemo) > n:
            return self.stepsMemo[n]
        
        result = self.steps(n-1) + self.steps(n-2)
        self.stepsMemo.append(result)

        return result
    
    def climbStairs(self, n: int) -> int:
        return self.steps(n)

main = Solution()
print(main.climbStairs(38))