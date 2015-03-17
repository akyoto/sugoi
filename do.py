#!/usr/bin/env python3

# Imports
from subprocess import call
import sys

cmd = sys.argv[1]

class Commands:
	def ls(args):
		call(["ls", "-la", "--color"])
		
	def install(args):
		riakUrl = "http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.5/ubuntu/trusty/riak_2.0.5-1_amd64.deb"
		print(args)
		print(riakUrl)

# Run the command
commands = Commands()
commands[cmd](args[2:])