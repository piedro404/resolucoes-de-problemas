
class Solution:
    def myAtoi(self, s: str) -> int:
        def isMathSignal(x):
            if x in ["-", "+"]:
                return True
            
            return False
        
        idc = 0
        for i, x in enumerate(s):
            if x != " ":
                idc = i
                break
            
        startId = -1
        number = ""
        for x in range(idc, len(s)):
            if (s[x].isdigit()):
                if startId == -1:
                    startId = x
                number += s[x]

            elif s[x].isalpha():
                break

            elif s[x] == ".":
                break

            elif x < len(s)-1:    
                if (number or (isMathSignal(s[x]) and not(s[x+1].isdigit()))):
                    break

            
        if not(number):
            number = "0"

        number2 = int(number)
        if startId > 0 and isMathSignal(s[startId-1]):
            number2 = int(s[startId-1] + str(number2))
        
        if number2 >= 2**31:
            number2 = (2**31)-1
        elif number2 < -(2**31):
            number2 = -(2**31)


        return number2

main = Solution()
print(main.myAtoi("     -42"))