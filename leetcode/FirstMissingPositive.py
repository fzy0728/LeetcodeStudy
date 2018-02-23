class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        while i<length:
            if(nums[i]!=i+1 and nums[i]>=1 and nums[i]<=length and nums[i]!= nums[nums[i]-1]):
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        for j in xrange(length):
            if nums[j]!=j+1:
                return j+1
        return length+1

if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([3,4,-1,1])
    print s.firstMissingPositive([1,2,0])
    print s.firstMissingPositive([2])
    print s.firstMissingPositive([2,3])
    print s.firstMissingPositive([-5,1000])
