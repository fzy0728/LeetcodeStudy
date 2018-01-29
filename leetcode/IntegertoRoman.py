class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = [["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["","X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["","M", "MM", "MMM"]]
        count = 0
        res = ''
        while(num>0):
            res = digit[count][num%10]+res
            num /= 10
            count+=1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(1034)
