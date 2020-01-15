class Solution:
    def median(self, n, nums):
        if n == 1:
            return nums[0]
        elif n % 2 == 0:
            return (nums[n//2 - 1] + nums[n//2])/2
        else:
            return nums[(n - 1)//2]
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:   # make sure nums1 is shorter
            nums1, nums2, m, n = nums2, nums1, n, m
        if m == 0:
            return self.median(n, nums2)
        imin, imax = 0, m
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    ml = nums2[j - 1]
                elif j == 0:
                    ml = nums1[i - 1]
                else:
                    ml = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return ml
                
                if i == m:
                    mr = nums2[j]
                elif j == n:
                    mr = nums1[i]
                else:
                    mr = min(nums1[i], nums2[j])
                    
                return (ml + mr) / 2.0
