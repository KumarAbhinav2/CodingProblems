class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        # Area will always be driven by the length of the smaller vertical line
        while i < j:
            if height[i] <= height[j]:
                cur_min_h = height[i]
                i += 1
            else:
                cur_min_h = height[j]
                j -= 1
            max_area = max(max_area, cur_min_h * (j - i + 1))
        return max_area

    # Time Complexity: O(n)
    # Space Complexity: O(1)
