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
    pass
def new_repo():
    pass
def repo_branches():
    pass
def commit_history():
    pass

def main():
    while True:
        print("Please enter what you want to do:")
        print("[1] See user repositories")
        print("[2] Create a new repo")
        print("[3] See a repositories branches")
        print("[4] See a repositories past commits")
        print("[5] Quit\n") 
       
        try:
            choice = int(input("Choice: ")) 
        except ValueError:
            print("Not a valid input\n")
            continue
        
        if choice not in range(1, 6):
            print("Not a valid input\n")
        else:
            if choice == 1:
                print("chose 1")
            elif choice == 2:
                print("chose 2")
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
