class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        target_list = []
        def combination(candidates,target,sum_list):
            if target == 0:
                target_list.append(sum_list)
            elif target > 0:
                for i in range(len(candidates)):
                    combination(candidates[i:], target - candidates[i], sum_list+[candidates[i]])
        combination(candidates,target,[])
        return target_list

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 6, 7],7)
