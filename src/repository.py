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
    def __init__(self, repo_name, description=""):
        self.name = repo_name
        self.description = description
        self.branches = None
        self.readme = None
        self.users = None

def main():
    repo_name = str(input("Name of repository:"))
    repo_desc = str(input("Brief Description:"))

    newrepo = repository(repo_name, repo_desc)
    print(newrepo.description)

if __name__ == "__main__":
    main()
