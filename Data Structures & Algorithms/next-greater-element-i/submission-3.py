class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        
        ptr=-1
        biggest=0
        for i in nums1:
            while ptr>-len(nums2) and nums2[ptr]!=i:
                if nums2[ptr]>i:
                    biggest=nums2[ptr]
                ptr-=1
            if biggest==0:
                result.append(-1)
            else:
                result.append(biggest)
            ptr=-1
            biggest=0
        
        return result
        
