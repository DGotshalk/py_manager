#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 drewtg <drewtg@The-Black-Star>
#
# Distributed under terms of the MIT license.

"""
"""
import sys
sys.path.append('./src')
from calls import github_api
from repository import repository

tokenfile = open('.mytoken', "r")
token = tokenfile.readline().split('\n')[0]
tokenfile.close()
user = 'dgotshalk'
mygit = github_api(user, token)



def user_repos():

    repo_json = mygit.user_repos().json()
    return  repo_json

def new_repo(repo):
    print(mygit.repo_start(repo))

def repo_branches():
    #output repos from user_repo(), put them into repo objects, and pass it to mygit.repo_branches(repo) 
    #mygit.repo_branches(repo)
    pass

def commit_history():
    #output repos from user_repo(), put them into repo objects, and pass it to mygit.repo_commits(repo) 
    #mygit.repo_commits(repo)
    pass

def main():
    while True:
        print("Please enter what you want to do:")
        print("[1] See user repositories")
        print("[2] Create a new repo")
        print("[3] See a repositories branches")
        print("[4] See a repositories past commits")
        print("[5] Quit") 
       
        try:
            choice = int(input("Choice: ")) 
        except ValueError:
            print("Not a valid input\n")
            continue
        
        if choice not in range(1, 6):
            print("Not a valid input\n")
        else:
            print()
            if choice == 1:
                request = user_repos()
                print("Repos:".ljust(30) + "Owner:".ljust(20) + "Private:")
                for repo in request:
                    print( (repo['name'] + ": ").ljust(30) +  (repo["owner"]["login"] + ", ").ljust(20) + str(repo["private"]))
            elif choice == 2:
                name = input("Name of new Repo: ")
                desc = input("Description of Repo: ")
                priv = input("private? (true/false)") # need to have better conditional loops in case someone puts bad answer:)
                repo = repository(name, desc, priv)
                new_repo(repo)

            elif choice == 3:
                print("chose 3")
            elif choice == 4:
                print("chose 4")
            elif choice == 5:
                print("Goodbye")
                print()
                break
            print()

if __name__ == "__main__":
    main()
