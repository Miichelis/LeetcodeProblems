class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        new_L=nums1+nums2
        sorted(new_L)
        if len(new_L)%2 == 0:
            mid=(len(new_L)/2+len(new_L)/2+1)/2
            median=(new_L[mid]+new_L[mid-1])/2.0
        else:
            mid=len(new_L)/2+1
            median=new_L[mid]
        
        return median


