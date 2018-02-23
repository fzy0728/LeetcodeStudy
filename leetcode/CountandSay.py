class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = '1*'
        for i in range(n-1):
            count = 1
            st = ''
            for j in range(1,len(s)):
                if s[j-1] == s[j]:
                    count+=1
                else:
                    st += str(count) + s[j-1]
                    count = 1
            s = st+'*'
        return s[0:len(s)-1]


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)