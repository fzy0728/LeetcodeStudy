class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        maxarea = 0
        while(l<r):
            maxarea =max(maxarea,min(height[r],height[l])*(r-l))
            if(height[r]>height[l]):
                l+=1
            else:
                r-=1
        return maxarea

if __name__=='__main__':
    s = Solution()
    print s.maxArea([1,2,3,4,5])