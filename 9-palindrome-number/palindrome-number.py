class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = int(len(x)/2)

        for i in range(n):
            print(i)
            if x[i] != x[-(i+1)]:
                return False

        return True
