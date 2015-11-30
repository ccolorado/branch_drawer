#!/usr/bin/env python2.7

import argparse
import ConfigParser
import io
import os
import os.path
import subprocess

# Check is there is an in repo config
# store a unique place per clone to store the drawer directory
# git config hook.yourhook.yourconfigval value

def get_repo_root_directory():
    repo_root_directory = subprocess.check_output( "git rev-parse --show-toplevel", shell = True )
    return repo_root_directory

def get_current_branch_name():
    # Remove extra line breaks and whitespaces
    current_branch_name = subprocess.check_output( "basename $(git symbolic-ref -q HEAD)", shell = True )
    # current_branch_name = subprocess.check_output( ["basename", current_branch_name] )
    return current_branch_name

def get_repo_name():
    # Figure out getting git reponame ( regarthless of the name of the repo root directory )
    repo_name = subprocess.check_output( 'git something', shell = True )
    return " idklol "

def parse_args():
    print(get_current_branch_name())
    print("x")

def main():
    global CONF
    CONF = parse_args()

if __name__ == '__main__':
    main()
