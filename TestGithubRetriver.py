import unittest
from HW04a_YuanZhang import GitHubRetriver


class testGitHubRetriver(unittest.TestCase):

    def testKybeth(self):
        # test if the number of repositories are right
        self.assertEqual(sorted(GitHubRetriver('Kybeth'))
                         [0], 'Courses-Related')
        self.assertEqual(GitHubRetriver('Kybeth')['auto-sms-by-twilio'], 3)


if __name__ == '__main__':
    # unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    # this runs all of the tests - use this line if running from the command line
    unittest.main(exit=True)
