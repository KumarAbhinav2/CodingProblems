class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return None
        oldColor = image[sr][sc]
        # If the new color is equal to the old color
        if newColor == oldColor:
            return image
        # all possible 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            # new point should be of old color
            if image[r][c] == oldColor:
                # assign new color
                image[r][c] = newColor
                for i, j in directions:
                    nr = i+r
                    nc = j+c
                    if 0<=nr<len(image) and 0<=nc<len(image[0]):
                        dfs(nr, nc)
        dfs(sr, sc)
        return image

    # Time Complexity: O(N) number of pixels in the image
    # Space Complexity: O(N) size of the implicit call stack when calling dfs

