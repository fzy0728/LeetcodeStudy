#coding:utf-8

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX_LVP = 0
        LVP = 0
        ValidList = []
        right = 0
        for i in range(len(s)):
            if(s[i] == '(' ):
                ValidList.append('(')
                right+=1
            if(s[i] == ')' ):
                if(right > 0 ):
                    right-=1
                    while(ValidList[len(ValidList)-1]!='('):
                        LVP+=ValidList.pop()
                    ValidList.pop()
                    LVP += 2
                    while(len(ValidList)!=0 and isinstance(ValidList[len(ValidList)-1],int)):
                        LVP += ValidList.pop()
                    if(LVP>MAX_LVP):
                        MAX_LVP = LVP
                    ValidList.append(LVP)
                    LVP = 0
                else:
                    if(LVP!=0):
                        ValidList.append(LVP)
                        LVP = 0
                    ValidList.append(')')
        return MAX_LVP


if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses("(()")
    print s.longestValidParentheses(")()())")
    print s.longestValidParentheses("()(()")
    print s.longestValidParentheses("(()())")
    print s.longestValidParentheses("(()()")
    print s.longestValidParentheses(")()())()()(")
    print s.longestValidParentheses("(()(((()")
    print s.longestValidParentheses(")(())(()()))(")
