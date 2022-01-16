class Solution:

    def get_rotate_index(self, nums, left, right):
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] > nums[pivot+1]:
                return pivot+1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1

    def _search(self, left, right, target, nums):
        while left <= right:
            pivot = (left+right)//2
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                left = pivot+1
            else:
                right = pivot-1
        return -1

    def search(self, nums, target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        rotate_index = self.get_rotate_index(nums, 0, len(nums)-1)

        if target == nums[rotate_index]:
            return rotate_index
        if rotate_index == 0:
            return self._search(0, len(nums)-1, target, nums)
        if target < nums[0]:
            return self._search(rotate_index, len(nums)-1, target, nums)
        return self._search(0, rotate_index, target, nums)

    # Time: O(logn)
    # Space: O(1)

obj = Solution()
print(obj.search([4, 5, 6, 7, 8, 1, 2, 3], 5))
