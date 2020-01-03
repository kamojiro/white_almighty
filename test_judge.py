import unittest

from tiles import tiles
from judgement import judge_decomposable

class JudgeTest(unittest.TestCase):
    def test(self):
        hands = [0, 0, 0, 0, 0, 1, 3, 3, 2, 3]
        self.assertTrue( judge_decomposable(hands))

if __name__=='__main__':
    unittest.main()
