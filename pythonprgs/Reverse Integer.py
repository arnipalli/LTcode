class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        temp = 0
        negative= x<0
        x = abs(x)
        if -2**31<= x <=2**31-1:
            while x!=0:
                temp = temp*10 + x%10
                x=x//10
            ans = temp if not negative else -(temp)
            if -2**31<= ans <=2**31-1:
                return ans
            return 0
        else:
            return 0