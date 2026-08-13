class Solution(object):
    def longestCommonPrefix(self, strs):
       res=""
       if len(strs)==0:
         return res
       if strs[0]=="":
         return res 
       for i in range(len(strs[0])):
        for s in strs :
            if i==len(s) or s[i]!=strs[0][i]:
                return res
        res+=strs[0][i]
       return res

        