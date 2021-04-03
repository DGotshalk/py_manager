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
"""

import requests

class github_api:
    def __init__(self, user):
        self.user_name = user

    # -u username:$token
    def repo_start(self, repo):
        url = 'https://api.github.com/'+ self.user_name+ "/" + repo.name + "/"
        headers = { "Accept":"application/vnd.github.v3+json"}
        requests.post(url,headers=headers) 
        pass          
    def repo_branches(self, repo):
        pass
    def repo_commits(self, repo):
        pass
