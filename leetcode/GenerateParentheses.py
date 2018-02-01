# coding:utf-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        #方法一
        # if (n == 0): return [""]
        # for i in xrange(n):
        #     for left in self.generateParenthesis(i):
        #         for right in self.generateParenthesis(n-i-1):
        #             ans.append('({}){}'.format(left,right))
        # return ans
        #方法二
        # def generatePDFS(s='',right=0,lift=0):
        #     if(len(s)==2*n):
        #         ans.append(s)
        #         return
        #     if(lift<n):
        #         generatePDFS(s+'(',right,lift+1)
        #     if(right<lift):
        #         generatePDFS(s+')',right+1,lift)
        # generatePDFS()
        self.partten(ans,'',n,n)
        return ans
    def partten(self,ans,s,right,lift):
        if(right==0 and lift==0):
            ans.append(s)
            return
        if(lift>0):
            self.partten(ans,s+'(',right,lift-1)
        if(right>lift):
            self.partten(ans,s+')',right-1,lift)


if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)