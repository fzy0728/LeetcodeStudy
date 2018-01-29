class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        length = len(str(x))
        num = 0
        for i in range(length/2):
            num = 10*num+x%10
            x = x/10
        print x
        print num
        if(x == num and length%2 ==0 ):
            return True
        elif(x/10 == num and length%2 == 1):
            return True
        else:
            return False
if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(12321)
    print s.isPalindrome(123321)
    print s.isPalindrome(10)