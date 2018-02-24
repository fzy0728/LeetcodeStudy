class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:return 0
        max_positive = 0
        for i in xrange(1,len(height)):
            if height[i]>height[max_positive]:
                max_positive = i
        i = 0
        sum_height = 0
        while i !=max_positive :
            temp = height[i]
            while height[i+1]<temp:
                sum_height+=(temp-height[i+1])
                i+=1
            i+=1
        i = len(height)-1
        while i !=max_positive :
            temp = height[i]
            while height[i-1]<temp:
                sum_height+=(temp-height[i-1])
                i-=1
            i-=1
        return sum_height

if __name__ == '__main__':
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print s.trap([])
    print s.trap([1,7,8])
    print s.trap([5,4,1,2])
    print s.trap([5,2,1,2,1,5])
