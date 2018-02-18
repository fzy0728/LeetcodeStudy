class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        temp = 0
        if(len(needle)==0):
            return 0
        for i in range(len(haystack)):
            if(len(haystack)-i>=len(needle)):
                for j in range(0,len(needle)):
                    if(haystack[i+j]!=needle[j]):
                        temp = -1
                        break
                    else:
                        temp = 1
            else:
                continue
            if(temp ==1):
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.strStr('hello','ll')
    print s.strStr('aaaaa','bba')
    print s.strStr('aaa','aaaa')
    print s.strStr('aaa','aaa')
    print s.strStr('a','a')
    print s.strStr('mississippi','issipi')