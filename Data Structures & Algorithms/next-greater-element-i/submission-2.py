class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[]
        for i in nums2:
            stack.append(i)
        
        ptr=-1
        biggest=0
        for i in nums1:
            while ptr>-len(stack) and stack[ptr]!=i:
                if stack[ptr]>i:
                    biggest=stack[ptr]
                ptr-=1
            if biggest==0:
                result.append(-1)
            else:
                result.append(biggest)
            ptr=-1
            biggest=0
        
        return result
        
