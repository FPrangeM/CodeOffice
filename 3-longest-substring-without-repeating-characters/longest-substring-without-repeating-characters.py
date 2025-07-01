class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        substring = ''


        for window_start in range(len(s)):
            window_end = window_start+1

            while window_end != len(s) and s[window_end] not in s[window_start:window_end]:
                window_end +=1

            if len(s[window_start:window_end]) > max_length:
                max_length = len(s[window_start:window_end])
            
            if window_end == len(s):
                break


        return max_length
