#!/usr/bin/env python2.7

import argparse
import ConfigParser
import io
import os
import os.path
import subprocess

# git config hook.yourhook.yourconfigval value

def get_repo_root_directory():
    repo_root_directory = subprocess.check_output( "git rev-parse --show-toplevel", shell = True )
    return repo_root_directory.strip()

def get_current_branch_name():
    current_branch_name = subprocess.check_output( "basename $(git symbolic-ref -q HEAD)", shell = True )
    return current_branch_name.strip()

def get_repo_name():
    repo_name = subprocess.check_output( "basename %s" % get_repo_root_directory(), shell = True )
    return repo_name.strip()

def parse_args():
    print("Repo Name : " + get_repo_name())
    print("Repo root directory : " + get_repo_root_directory())
    print("Current Branch : " + get_current_branch_name())

def main():
    global CONF
    CONF = parse_args()

if __name__ == '__main__':
    main()
