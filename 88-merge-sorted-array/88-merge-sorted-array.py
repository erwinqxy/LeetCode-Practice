class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge from the back
        sizeN1 = m + n 
        
        n1Pointer = m - 1
        n2Pointer = n - 1
        for i in range (sizeN1): 
            if (n1Pointer < 0):
                for i in range (n2Pointer+1):
                    nums1[i] = nums2[i]
                break
            if (n2Pointer < 0):
                break
            if (nums1[n1Pointer] > nums2[n2Pointer]):
                nums1[sizeN1-i-1] = nums1[n1Pointer]
                n1Pointer -= 1
            elif (nums1[n1Pointer] <= nums2[n2Pointer]):
                nums1[sizeN1-i-1] = nums2[n2Pointer]
                n2Pointer -= 1
        return nums1



    ## cleaner almost similiar [for reference]
#         def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        
#         # Set p1 and p2 to point to the end of their respective arrays.
#         p1 = m - 1
#         p2 = n - 1
    
#         # And move p backwards through the array, each time writing
#         # the smallest value pointed at by p1 or p2.
#         for p in range(n + m - 1, -1, -1):
#             if p2 < 0:
#                 break
#             if p1 >= 0 and nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1