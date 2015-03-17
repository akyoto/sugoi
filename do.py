#!/usr/bin/env python3

# Imports
from subprocess import call
import sys

# Commands
class Commands:
	def ls(args):
		call(["ls", "-la", "--color"] + args)
		
	def info(args):
		call(["uname", "-a"])
		call(["uptime"])
		call(["free", "-m"])
		
	def update(args):
		call(["sudo", "apt-get", "update"])
		call(["sudo", "apt-get", "upgrade"])
		
	def install(args):
		vars(Install)[args[0]](args[1:])
		
	def __getitem__(self, name):
		return getattr(self, name)

# Package installations
class Install:
	def riak(args):
		riakUrl = "http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.5/ubuntu/trusty/riak_2.0.5-1_amd64.deb"
		call(["wget", riakUrl])

# Help
def showHelp():
	print("Commands:")
	print(["\t" + cmd + "\n" for cmd in vars(Commands)])

# Command line arguments
args = sys.argv[1:]

# Help?
if not args:
	showHelp()
	sys.exit(1)

# Parameters
cmd = args[0]
subArgs = args[1:]

# Run the command
vars(Commands)[cmd](subArgs)