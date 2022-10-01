class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num<10:
                return num
            temp=0
            while num!=0:
                temp = temp+(num%10)
                num=num//10
            num = temp