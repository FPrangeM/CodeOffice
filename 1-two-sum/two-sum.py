class Solution(object):
    def twoSum(self, nums, target):
        # nums = [lambda x: x if x <= target else 0.1 for x in nums]

        n = len(nums)
        s = 0

        for i1 in range(n):
            for i2 in range(i1+1,n):
                n1=nums[i1]
                n2=nums[i2]
                s = n1+n2
                if s == target:
                    return [i1,i2]

