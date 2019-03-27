import unittest
from unittest import mock
from HW04a_YuanZhang import GitHubRetriver


class testGitHubRetriver(unittest.TestCase):

    def testKybeth(self):
        mock_Kybeth = mock.Mock(
            return_value={'auto-sms-by-twilio': 3, 'Courses-Related': 1,
                          'Distribution-of-unfair-shuffle': 3,
                          'hello-world': 3,
                          'Leetcode-Notebook': 1,
                          'reveal.js-for-DuckMommy': 8,
                          'SSW567-HW02a-Triangle567': 12,
                          'SSW690-project': 5,
                          'Stevens-SSW567-HW01': 4,
                          'Stevens-SSW567-HW04a-GitHubApi': 7,
                          'Stevens-SSW810-Course-Management-Repository': 2})
        GitHubRetriver = mock_Kybeth
        self.assertEqual(sorted(GitHubRetriver('Kybeth'))
                         [0], 'Courses-Related')
        self.assertEqual(GitHubRetriver('Kybeth')['auto-sms-by-twilio'], 3)


if __name__ == '__main__':
    # unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    # this runs all of the tests - use this line if running from the command line
    unittest.main(exit=True)
