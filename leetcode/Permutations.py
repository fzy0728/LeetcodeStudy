class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def permute(nums,num,list_nums):
            if len(num) == len(nums):
                res.append(list_nums)
            for i in range(len(nums)):
                if i in num:
                    continue
                permute(nums,num+[i],list_nums+[nums[i]])
        permute(nums,[],[])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3,4])
    print s.permute([1,2,3])
    print s.permute([1,2])
    print s.permute([1])
    print s.permute([])


