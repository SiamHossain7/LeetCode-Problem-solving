class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        arr=nums1+nums2
        arr.sort()
        total=len(arr)
        if total%2==1:
            return float(arr[total//2])
        else:
            arr1=arr[total//2-1]
            arr2=arr[total//2]
            return (float(arr1) +float(arr2))//2
        
s = Solution()
result = s.findMedianSortedArrays([1,2], [3,4])
print(result)