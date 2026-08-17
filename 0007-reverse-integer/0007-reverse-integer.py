class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        sign=1
        s=str(x)
        if s[0]=="-":
            sign=-1
            s=s[1:]
        x=int(s)
        while(x>0):
            d=x%10
            rev=rev*10+d
            x=x//10
        rev=rev*sign
        if(rev<-2**31 or rev>2**31+1):
            return 0
        return rev
        