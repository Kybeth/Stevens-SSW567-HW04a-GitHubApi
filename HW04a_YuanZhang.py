# -*- coding: utf-8 -*-
"""
Author: Yuan Zhang
Course: SSW 567
Description of this script: HW04a - Develop with the Perspective of the Tester in mind
"""

import urllib.request
import json


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
            commit_url = 'https://api.github.com/repos/{}/{}/commits'.format(
                user_id, repo_name)
            urlhand = urllib.request.urlopen(commit_url)
            data = urlhand.read().decode()
            info = json.loads(data)
            commits_num = len(info)
            repo_pair[repo_name] = commits_num
        return repo_pair


def run_GitHubRetriver(user_id):
    print("---Below shows the repositories and the number of commits of {}---".format(user_id))
    dic = GitHubRetriver(user_id)
    for key in dic:
        print('{}: {}'.format(key, dic[key]))


if __name__ == '__main__':
    run_GitHubRetriver('richkempinski')
