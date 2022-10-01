class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == " " :
            return 0
        else:
            p=s.strip().split(" ")
            return (len(p[-1]))