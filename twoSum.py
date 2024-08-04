class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {val:idx for idx,val in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict and nums_dict[complement] != i:
                return [i,nums_dict[complement]]

s = Solution()    
print(s.twoSum([3,3],6))
        