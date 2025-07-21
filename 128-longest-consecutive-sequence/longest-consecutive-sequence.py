class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if not nums:
            return 0

        elif len(nums) == 1:
            return 1

        else:
            sorted_list = sorted(list(set(nums)))
            previous = sorted_list[0]

            sequence = 1
            max_sequence = 1

            for i in range(1,len(sorted_list)):
                num = sorted_list[i]

                if num == previous+1:
                    sequence+=1

                else:
                    max_sequence=max(max_sequence,sequence)
                    sequence=1

                previous=num

            max_sequence=max(max_sequence,sequence)
            
            return max_sequence
