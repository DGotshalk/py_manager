#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 drewtg <drewtg@The-Black-Star>
#
# Distributed under terms of the MIT license.

"""
This file is where we will be doing the github calls,
This file will be used by the repos class to update all the inforamtion within the class
https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
https://docs.github.com/en/rest/reference
https://curl.trillworks.com/#python
"""

import requests

class github_api:
    def __init__(self, user, token=""):
        self.user_name = user
        self.json_header = {"Accept":"application/vnd.github.v3+json"}
        self.token = token 
    def user_repos(self):
        """Returns a list of user repositories"""
        url = 'https://api.github.com/users/' + self.user_name + '/repos'
        request = requests.get(url,headers=self.json_header) 
        return request
    
    # -u username:$token
    def repo_start(self, repo):
        """Creates a new repository"""
        url = 'https://api.github.com/user/repos'
        header = {"Accept":"application/vnd.github.v3+json",
                "Authorization" : 'token ' + self.token} 
        data = '{"name" : "' + repo.name + '"}' 
        print(data) 
        request = requests.post(url, headers=header, data=data)
        return request
    
    def repo_branches(self, repo):
        """See current branches (description of branches if that is a thing) as well as last commits on branches"""
        url = 'https://api.github.com/repos/' + self.user_name + '/' + repo.name + '/branches'
        request = requests.get(url, headers=self.json_header)
        return request 

    def repo_commits(self, repo):
        """View commit history of repository (have to decide what branches I would be looking at)"""
        request = "" 
        return request 
