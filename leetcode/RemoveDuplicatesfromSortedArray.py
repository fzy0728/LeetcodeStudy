class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 0
        i = 0
        for j in nums:
            if(nums[i]!=j):
                i+=1
                nums[i]=j
        return i+1

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,2,2,3])

