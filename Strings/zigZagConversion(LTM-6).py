"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

"""

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows > len(s):
            return s
        l = ['']*numRows
        # index to move across columns and step across row
        index, step = 0,0

        for char in s:
            l[index] += char
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return ''.join(l)

    # Time Complexity: O(n) , n be the chars in string
    # Space Complexity: O(n), extra space
