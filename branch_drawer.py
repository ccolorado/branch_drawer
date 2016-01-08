#!/usr/bin/env python2.7

import argparse
import ConfigParser
import io
import os
import os.path
import subprocess

DEFAULTS = """
[branch_drawer]
# Location of drawer repo
drawer_dir=~/.branch_drawer.d
# Drawer Name
drawer_link_name=Branch_Drawer
"""
# git config hook.yourhook.yourconfigval value
def create_conf():
    user_config = CONFIG_FILES[-1]
    if not os.path.exists(user_config):
        with open(user_config, 'w') as f:
            f.write(DEFAULTS)

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

    conf_parser = argparse.ArgumentParser(add_help=False)
    conf_parser.add_argument('--conf-file', '-c', help='Specify the config file')

    args, remaining = conf_parser.parse_known_args()
    config = ConfigParser.RawConfigParser()

    config.readfp(io.BytesIO(DEFAULTS))
    if args.conf_file:
        config.read([args.conf_file])
    else:
        create_conf()
        config.read(CONFIG_FILES)

    opts = dict(config.items('branch_drawer'))
    parser = argparse.ArgumentParser(parents=[conf_parser])
    parser.set_defaults(**opts)

    parser.add_argument('--drawer_dir', '-d', help='Drawer storage location')
    parser.add_argument('--drawer_link_name', '-l', help='In repo drawer link name')

    args = parser.parse_args()
    args.drawer_dir = args.drawer_dir or os.environ.get('drawer_dir') or opts['drawer_dir']
    args.drawer_link_name = args.drawer_link_name or os.environ.get('drawer_link_name') or opts['drawer_link_name']

    return args

def main():
    global CONF
    CONF = parse_args()

CONFIG_FILES = ['/etc/branch_drawer', os.path.join(os.path.expanduser('~'), '.branch_drawer') ]

if __name__ == '__main__':
    main()
