#!/usr/bin/env python3

# Imports
import subprocess
import sys

call = subprocess.call
Popen = subprocess.Popen

# Commands
class Commands:
	def ls(args):
		call(["ls", "-la", "--color"] + args)
		
	def info(args):
		print("Kernel:")
		call(["uname", "-a"])
		
		print("\nUptime:")
		call(["uptime"])
		
		def showMemory(grepString):
			meminfo = Popen(["cat", "/proc/meminfo"], stdout = subprocess.PIPE)
			grep = Popen(["grep", grepString], stdin = meminfo.stdout, stdout = subprocess.PIPE)
			sys.stdout.write(grep.communicate()[0].decode("utf-8"))
		
		print("\nMemory:")
		showMemory("Mem")
		showMemory("Buffers")
		showMemory("Cached")
		
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
		call(["mkdir", "~/apps/"])
		call(["git", "clone", "git://github.com/basho/riak.git", "~/apps/"])
		call(["cd", "~/apps/riak"])
		call(["make", "rel"])
cd riak
make rel

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