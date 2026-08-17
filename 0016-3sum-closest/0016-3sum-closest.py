class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        actualsum=float('inf')
        for i,a in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                threesum=a+nums[l]+nums[r]
                if(abs(threesum-target)<abs(actualsum-target)):
                    actualsum=threesum
                elif(threesum==target):
                    return threesum
                if(threesum<target):
                    l+=1
                else:
                    r-=1
        return actualsum
        