"""
Author: Yuan Zhang
Course: SSW 567
Description of this script: HW04a - Develop with the Perspective of the Tester in mind
"""

import urllib.request
import json
import unittest 

def GitHubRetriver(user_id):
    repo_url = 'https://api.github.com/users/{}/repos'.format(user_id)
    try:
        urlhand = urllib.request.urlopen(repo_url)
    except ValueError:
        print('The GitHub API cannot be opened. Please check your input or the availability of the website')
    else:
            data = urlhand.read().decode()
            info = json.loads(data)
            repo_pair = {}
            for repo in info:
                repo_name = repo["name"]
                commit_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_id, repo_name)
                urlhand = urllib.request.urlopen(commit_url)
                data = urlhand.read().decode()
                info = json.loads(data)
                commits_num = len(info)
                repo_pair[repo_name] = commits_num
            return repo_pair
            

def run_GitHubRetriver(user_id):    
    print("---Below shows the user's repositories and their number of commits---")
    dic = GitHubRetriver(user_id)
    for key in dic:
        print('[Repo] {} [Number of commits] {}'.format(key, dic[key]))
    
    

class testGitHubRetriver(unittest.TestCase):
    
    def testKybeth(self):
        self.assertEqual(len(GitHubRetriver('Kybeth')), 9) # test if the number of repositories are right
        self.assertEqual(sorted(GitHubRetriver('Kybeth'))[0], 'Courses-Related')
        self.assertEqual(GitHubRetriver('Kybeth')['auto-sms-by-twilio'], 3)
  
    def testrichkempinski(self):
        self.assertDictEqual(GitHubRetriver('richkempinski'), {'hellogitworld': 30, 'helloworld': 6, 'Mocks': 9, 'Project1': 2, 'threads-of-life': 1})
    


if __name__ == '__main__':
    # examples of running the code
    run_GitHubRetriver('richkempinski')
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    