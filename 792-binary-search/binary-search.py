class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        center_index = int((left+right)/2)
        center = nums[center_index]

        D={}

        while target not in [nums[left],center,nums[right]]:

            center_index = int((left+right)/2)
            center = nums[center_index]
            D[center] = D.get(center,0) + 1

            if D.get(center,0) >= 2:
                return -1
                break

            if target > center:
                left = center_index
            else:
                right = center_index
            
            print(D)

        for index in [left,center_index,right]:
            if nums[index] == target:
                return index
