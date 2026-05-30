class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1

        left=0
        right=len(nums1)

        while left<=right:
            cut1=(left+right)//2
            cut2=(len(nums1)+len(nums2))//2-cut1
            left1  = nums1[cut1-1] if cut1 > 0        else float('-inf')
            right1 = nums1[cut1]   if cut1 < len(nums1) else float('inf')
            left2  = nums2[cut2-1] if cut2 > 0        else float('-inf')
            right2 = nums2[cut2]   if cut2 < len(nums2) else float('inf')

            if(left1<right2 and left2<right1):
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(right1, right2)      
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif(left1>right2):
                right=cut1-1
            else:
                left=cut1+1

        return 0