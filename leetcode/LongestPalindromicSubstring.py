
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        Str = ''
        Max = 0
        for length in range(1,len(s)+1):
            for i in range(len(s)-length+1):
                j = i+length
                if(self.reversedStr(s[i:j])):
                    if(Max<length):
                        Max = length
                        Str = s[i:j]

        return Str

        # start = 0
        # MaxLength = 0
        # dp = [[False for i in range(len(s))] for i in range(len(s))]
        # if(len(s)==1):
        #     return s
        # for i in range(len(s)):
        #     dp[i][i] = True
        #     if(i<len(s)-1 and s[i] == s[i+1]):
        #         dp[i][i+1] = True
        #         start = i
        #         MaxLength = 2
        # for length in range(3,len(s)+1):
        #     for i in range(len(s)-length+1):
        #         j = i+length-1
        #         if(s[j]==s[i] and dp[i+1][j-1]):
        #             dp[i][j] = True
        #             MaxLength = length
        #             start = i
        # if(MaxLength>=2):
        #     return s[start:start+MaxLength]
        # return s[0]


    def reversedStr(self,s):
        for i in range(len(s)):
            if(s[i] != s[len(s)-i-1]):
                return False
        return True

if __name__ == '__main__':

    s = Solution()
    print s.longestPalindrome('aba')
    print s.longestPalindrome('a')
    #print s.reversedStr('aba')
    print s.longestPalindrome('ababa')
    print s.longestPalindrome('abba')
    print s.longestPalindrome('cbba')
    print s.longestPalindrome('abcda')
    #print s.reversedStr('ababa')