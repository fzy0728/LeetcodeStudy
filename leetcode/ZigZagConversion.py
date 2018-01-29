# 1   5   9
# 2 4 6 8 10             3
# 3   7   11
#
# 1     7       13
# 2 5   8 11    14       4
# 3   6 9    12 15
# 4     10      16

# 1       9           17
# 2 6     10 14       18
# 3   7   11    15    19  5
# 4     8 12       16 20
# 5       13          21
#
# 1
# 2  8
# 3     9                 7
# 4       10
# 5           11
# 6               12
# 7

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        Slength = len(s)
        newStr = ''
        jump = numRows*2-2
        if(numRows>=Slength or numRows == 1):
            return s
        for i in range(numRows):
            temp = 1
            count = i
            if(i==0 or i==numRows-1):
                while(count<Slength):
                    newStr += s[count]
                    count+=jump
            else:
                if(temp == 1):
                    row = 2*i-numRows+1
                    stage = jump/2-row
                while (count < Slength):
                    temp = 0
                    newStr += s[count]
                    count += stage
                    stage = jump-stage
        return newStr

if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("A", 1)
    print s.convert("ABCDE", 4)
    print s.convert("PAYPALISHIRING",4)



