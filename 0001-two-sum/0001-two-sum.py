class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return "Sum not found"
s1=Solution()
s2=Solution()
s3=Solution()
print(s1.twoSum([2,7,11,15],9))
print(s2.twoSum([3,2,4],6))
print(s3.twoSum([3,3],6))   