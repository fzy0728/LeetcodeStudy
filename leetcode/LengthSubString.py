class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        temp = -1
        res = 0

        for i in range(len(s)):
            for j in range(start,end):
                if(s[j]==s[i]):
                    temp = j+1
            if(temp == -1):
                end += 1
                res = max(res,end-start)
            else :
                start = temp
                end += 1
                temp = -1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring('abcabcbb')
    print s.lengthOfLongestSubstring('bbbbb')
    print s.lengthOfLongestSubstring('pwwkew')
    print s.lengthOfLongestSubstring('dvdf')
    print s.lengthOfLongestSubstring('')
    print s.lengthOfLongestSubstring('a')
    print s.lengthOfLongestSubstring('ab')
    print s.lengthOfLongestSubstring('abb')
    print s.lengthOfLongestSubstring('abbb')