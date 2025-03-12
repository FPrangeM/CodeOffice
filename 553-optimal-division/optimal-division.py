class Solution:
    def optimalDivision(self, nums: List[int]) -> str:


        nstr = '/'.join([str(n) for n in nums])
        if len(nums) >= 3:
            nstr = nstr.replace('/',"/(",1)+')'

        return nstr