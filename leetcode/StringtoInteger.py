class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sum = 0
        dight = 1
        count = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.strip()
        if (len(str)==0):
            return 0
        if (str[0] == '-'):
            dight = -1
            count = 1
        if (str[0] == '+'):
            dight = 1
            count = 1
        for i in range(count,len(str)):
            num = ord(str[i])-ord('0')
            if(num>=10 or num<0):
                break
            sum = sum*10+num
            if int.bit_length(sum)>32:
                break
        if(int.bit_length(sum*dight)<32):
            return sum*dight
        else:
            if(dight>0):
                return INT_MAX
            else:
                return INT_MIN

if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("+1")
    print s.myAtoi("+123")
    print s.myAtoi("-123   ")
    print s.myAtoi("    -123   ")
    print s.myAtoi("    -12 3   ")
    print s.myAtoi(" -0012a42")
    print s.myAtoi(" +-2")
    print s.myAtoi(" -+2")
    print s.myAtoi("2147483648")
    print s.myAtoi("-2147483647")
    print s.myAtoi("9223372036854775809")