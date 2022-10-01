class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1 or n==2):
            return 1
        else:
            first=1
            second=1
            third=0
            for i in range(3,n+1):
                third = first + second
                first = second
                second = third
        return(second)