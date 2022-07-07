class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shortArray = nums1 if len(nums1) <= len(nums2) else nums2
        longerArray = nums1 if len(nums1) > len(nums2) else nums2
        
        intersect = [] 
        for x in shortArray:
          if (x in longerArray):
            intersect.append(x)
            longerArray.remove(x)
        return intersect 

        