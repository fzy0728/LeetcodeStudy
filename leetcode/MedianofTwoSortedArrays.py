class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        if(m>n):
            nums1,nums2,m,n = nums2,nums1,n,m
        imin = 0
        imax = m
        halflen = (n+m+1)/2
        while(imin <= imax):
            i = (imin+imax)/2
            j = halflen - i
            if(i<imax and nums1[i]<nums2[j-1]):
                imin = i+1
            elif(i>imin and nums2[j]<nums1[i-1]):
                imax = i-1
            else:
                maxleft = 0
                if(i==0):
                    maxleft = nums2[j-1]
                elif(j==0):
                    maxleft = nums1[i-1]
                else:
                    maxleft = max(nums1[i-1],nums2[j-1])
                if((n+m)%2==1):
                    return maxleft
                minright = 0
                if(i == m):
                    minright = nums2[j]
                elif(j == n):
                    minright = nums1[i]
                else:
                    minright = min(nums1[i],nums2[j])

                return (minright+maxleft)/2.0
if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,3,4],[5,6,7,8])