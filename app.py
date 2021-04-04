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


mygit = github_api('dgotshalk', token)

