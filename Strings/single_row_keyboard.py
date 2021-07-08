class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        steps = 0
        last_index = 0
        key_map = {}
        for i,val in enumerate(keyboard):
            key_map[val] = i
        for val in word:
            index = key_map[val]
            steps += abs(index - last_index)
            last_index = index
        return steps


obj = Solution()
print(obj.calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"))
print(obj.calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"))