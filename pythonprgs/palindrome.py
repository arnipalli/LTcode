class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = x
        temp =0 
        while y!=0:
            temp = temp*10 + y%10
            y = y//10
        return x == temp