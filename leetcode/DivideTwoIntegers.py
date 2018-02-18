class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        div = 0
        digit = 1
        if((dividend<0 and divisor>0 )or(dividend>0 and divisor<0)):
            digit = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if(divisor>dividend):
            return 0
        while(divisor<=dividend):
            count = 0
            while(divisor<<count+1<dividend):
                count+=1
            #print "start divisor:",divisor," dividend:",dividend," count:",count
            div += 1<<count
            dividend = dividend-(divisor<<count)
            #print "end divisor:", divisor, " dividend:", dividend, " count:", count
        if(int.bit_length(div)<32):
            return div*digit
        else:
            if(digit<0):return INT_MIN
            else:return INT_MAX


if __name__ == '__main__':
    s = Solution()
    print s.divide(24,5)
    print s.divide(125,5)
    print s.divide(-2147483649,1)
    print s.divide(2147483649,1)