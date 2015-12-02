class Solution(object):
    def recursive_find_k(self,nums1,nums2,k):
        if(len(nums1)<len(nums2)):
            return self.recursive_find_k(nums2,nums1,k);
        if(len(nums2)==0):
            return nums1[k];
        if(k==0):
            return min(nums1[0],nums2[0]);
        len1=len(nums1);
        len2=len(nums2);
        step=min((k+1)/2,len2);
        if(nums1[k-step]<nums2[step-1]):
            return self.recursive_find_k(nums1[k-step+1:],nums2[:],step-1);
        else:
            return self.recursive_find_k(nums1[:],nums2[step:],k-step);
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1);
        len2=len(nums2);
        if((len1+len2)%2==1):
            return self.recursive_find_k(nums1,nums2,(len1+len2)/2);
        else:
            return (self.recursive_find_k(nums1,nums2,(len1+len2)/2)+\
                    self.recursive_find_k(nums1,nums2,(len1+len2)/2-1))*0.5
instance=Solution();
nums1=[1];
print nums1;
nums2=[2,3,4];

print instance.findMedianSortedArrays(nums1,nums2);