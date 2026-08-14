class Solution(object):
    def containsDuplicate(self, nums):
        charSet=set(nums)
        if (len(nums)==len(charSet)):
            return False
        else:
            return True
        