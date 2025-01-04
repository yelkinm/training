class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # yes, it's ugly, but it fast
        res =[]
        res = nums1 + nums2
        res.sort()
        l = len(res)
        print(res)
        print (l//2)
        if l%2 == 0 :
            return((res[l//2-1]+ res[(l//2)])/2)
            
        else: 
            return(res[l//2])
        
        
x = Solution()
r = x.findMedianSortedArrays([1,2,8], [1,10])
print (r)