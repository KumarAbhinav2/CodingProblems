class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

    def findKthLargest2(self, nums, k):
        # using bubble sort
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]

    def findKthLargest3(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


obj = Solution()
print(obj.findKthLargest([3,2,3,1,2,4,5,5,6], 4))