class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        n = len(str_x)

        for i in range((n//2)):
            if str_x[i] != str_x[-(i+1)]:
                return False
        return True
