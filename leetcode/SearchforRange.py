# coding:utf-8

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        start,end,middle = self.halfSearch(0,len(nums)-1,nums,target)
        #print start,end,middle
        start_target = middle
        end_target = middle
        if start == -1:
            return [-1,-1]
        #找左侧
        while start<start_target :
            temp = (start+start_target)/2
            #print temp
            if(nums[temp] == target):
                start_target = temp
            if(nums[temp] <target):
                start = temp+1
        #找右侧
        while end>end_target:

            temp = (end+end_target+1)/2
            if(nums[temp] == target):
                end_target = temp
            if(nums[temp] >target):
                end = temp-1


        return [start_target,end_target]


    def halfSearch(self,start,end,nums,target):

        middle = (start + end)/2

        if(nums[middle] == target):
            return start,end,middle
        if(start>=end):
            return -1,-1,-1
        elif(nums[middle] <= target):

            return self.halfSearch(middle+1,end,nums,target)

        else:

            return self.halfSearch(start,middle-1,nums,target)


if __name__ == '__main__':
    s = Solution()
    print s.searchRange([5, 7, 7, 8, 8, 10],8)
    print s.searchRange([5, 7, 7, 8, 8, 10],1)
    print s.searchRange([2,2],2)
    print s.searchRange([2,2,2],2)
    print s.searchRange([],1)