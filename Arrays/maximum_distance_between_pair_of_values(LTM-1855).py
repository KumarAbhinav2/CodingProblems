
class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        max_dist = 0
        for i, vi in enumerate(nums1):
            for j, vj in enumerate(nums2):
                if vj >= vi:
                    curr_dist = j-i
                    max_dist = max(max_dist, curr_dist)
                else:
                    break
        return max_dist

    def maxDistance2(self, nums1, nums2) -> int:
        max_dist  = 0
        i,j = 0,0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j] and i<=j:
                curr_dist = j - i
                max_dist = max(max_dist, curr_dist)
                j+=1
            else:
                i+=1
                j+=1

        return max_dist




obj = Solution()
print(obj.maxDistance2([55,30,5,4,2], [100,20,10,10,5]))
print(obj.maxDistance([30,29,19,5], [25,25,25,25,25]))