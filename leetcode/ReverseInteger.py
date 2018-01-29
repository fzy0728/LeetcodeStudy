class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        minus = 1
        if(x<0):
            x = -x
            minus = -1
        while(x!=0):
            num = num*10+x%10
            x = x/10
        if(int.bit_length(num)<32):
            return num*minus
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print s.reverse(120)
    print s.reverse(-120)
    print s.reverse(-123)
    print s.reverse(1534236469)
