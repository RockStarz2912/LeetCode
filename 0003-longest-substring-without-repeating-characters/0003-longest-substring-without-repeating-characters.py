class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=0
        l=0
        charset=set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            count=max(count,r-l+1)
        return count



        
        