#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 drewtg <drewtg@The-Black-Star>
#
# Distributed under terms of the MIT license.

"""
This class is going to represent a repository 
"""

class repository:
    def __init__(self, name, url, description="", branches=""): 
        self.name = name
        self.url = url
        self.description = description
        self.branches = branches

def main():
    repo_name = str(input("Name of repository:"))
    repo_url = str(input("URL ending of repository:"))
    repo_desc = str(input("Brief Description:"))

    newrepo = repository(repo_name, repo_url, repo_desc)
