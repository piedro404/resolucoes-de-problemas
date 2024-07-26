class Solution:
    def reverse(self, x: int) -> int:
        subX = int(str(abs(x))[::-1])
        if -2147483648 < subX < 2147483648:
            if x < 0: 
                return subX * -1

            return subX

        return 0 
        
    
main = Solution()
print(main.reverse(123))