class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        num = nums2+nums1
        num = sorted(num)

        if(len(num)%2==0):
            return (num[len(num)/2-1]+num[len(num)/2])/2.0
        else:
            return num[len(num)/2]

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,3],[4,5,6])