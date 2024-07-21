class Solution:
    def __init__(self) -> None:
        self.parenthesis = []
    def generate(self, n, c, o, ot, p):
        if c < n:
            if(ot < n):
                self.generate(n, c, o+1, ot+1, p+"(")
            if(o > 0):
                self.generate(n, c+1, o-1, ot, p+")")
        else:
            self.parenthesis.append(p)

    def generateParenthesis(self, n: int) -> list[str]:
        self.generate(n, 0, 1, 1, "(")
        return self.parenthesis

main = Solution()
print(main.generateParenthesis(3))