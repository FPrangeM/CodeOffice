class Solution:
    # O(n^2)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        for i1 in range(len(nums)):
            for i2 in range(i1+1,len(nums)):
                if nums[i1]+nums[i2] == target:
                    return [i1,i2]
        return None

    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seem={}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seem:
                return [i,seem[complement]]
            else:
                seem[num] = i
