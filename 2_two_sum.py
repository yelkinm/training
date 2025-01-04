class Solution(object):
    def twoSum(self, nums, target):
        # if elemen les then target try find matched element.
        # run inner loop by other elements. Should avoid element from outer loop
        for idx, val in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx!=idx2 and val + val2 == target:
                    return (idx,idx2)
                
# x= Solution()
# print(x.twoSum( [1,2,3,4,5], 9))