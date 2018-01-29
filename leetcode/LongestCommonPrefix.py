class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        res = ""
        if(length==1):
            return strs[0]
        for i in range(length-1):
            j = 0
            res = ""
            if(strs[i]==""or strs[i+1]==""):
                res = ""
                break
            while(strs[i][j] == strs[i+1][j]):
                res+=strs[i][j]
                if(j<len(strs[i])-1 and j<len(strs[i+1])-1):
                    j+=1
                else:
                    break
            strs[i+1] = res
            # print j
            # print strs
        return res
if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(["leets","leetcode","leet","leeds"])
    print s.longestCommonPrefix(["",""])
    print s.longestCommonPrefix([])
    print s.longestCommonPrefix(["a"])
