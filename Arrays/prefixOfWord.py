from duration import duration
import unittest


class Solution:

    @duration
    def prefixSearch(self, sentence, searchWord):
        """Without Using BuiltIn Functions"""
        word_pos = 1
        j = 0
        fresh_word = True
        for i in sentence:
            if i == ' ':
                word_pos += 1
                j = 0
                fresh_word = True
                continue
            if i == searchWord[j] and fresh_word:
                j += 1
            else:
                j = 0
                fresh_word = False
                continue
            if j >= len(searchWord):
                return word_pos
        return -1

    @duration
    def intuitive(self, sentence, searchWord):
        for index, i in enumerate(sentence.split(' ')):
            if i.startswith(searchWord):
                return index+1
        return -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1, self.input2 = "hello from the other side", "they"
        self.input3, self.input4 = "jonathan dumb", "dumb"
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1, self.input2)
        self.assertEqual(res, -1)
        res = self.obj.intuitive(self.input3, self.input4)
        self.assertEqual(res, 2)

    def test_better(self):
        res = self.obj.prefixSearch_withoutUsingBuiltInFunctions(self.input1, self.input2)
        self.assertEqual(res, -1)
        res = self.obj.prefixSearch_withoutUsingBuiltInFunctions(self.input3, self.input4)
        self.assertEqual(res, 2)


if __name__ == '__main__':
        unittest.main()