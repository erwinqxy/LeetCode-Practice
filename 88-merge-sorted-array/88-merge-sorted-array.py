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


            
                
        
#         if (m == 0): # if num1 is empty array, just need copy num2 over 
#             for i in range(n):
#                 nums1[i] = nums2[i]
#             return nums1
#         if (n == 0): # if num2 is empty array, just return num1
#             return nums1
        
#         # merging step 
#         for i in range(m):
#             # use the second array as temp, keep swapping the first element 
#             if(nums1[i] > nums2[0]):
#                 temp = nums1[i]
#                 nums1[i] = nums2[0]
#                 nums2[0] = temp 
#                 nums2.sort()

#         # now combine the two 
#         for i in range(n):
#             nums1[n+i] = nums2[i]
#         return nums1


            