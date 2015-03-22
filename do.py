#!/usr/bin/env python3

# Imports
import subprocess
import sys
import os

call = subprocess.call
Popen = subprocess.Popen

# Commands
class Commands:
	def ls(args):
		call(["ls", "-la", "--color"] + args)
		
	def tune(args):
		def sysctl(param):
			call(["sudo", "sysctl", param])
		
		sysctl("vm.swappiness=0")
		sysctl("net.ipv4.tcp_max_syn_backlog=40000")
		sysctl("net.core.somaxconn=40000")
		sysctl("net.core.wmem_default=8388608")
		sysctl("net.core.rmem_default=8388608")
		sysctl("net.ipv4.tcp_sack=1")
		sysctl("net.ipv4.tcp_window_scaling=1")
		sysctl("net.ipv4.tcp_fin_timeout=15")
		sysctl("net.ipv4.tcp_keepalive_intvl=30")
		sysctl("net.ipv4.tcp_tw_reuse=1")
		sysctl("net.ipv4.tcp_moderate_rcvbuf=1")
		
		# TODO: Save settings permanently
		# TODO: noatime in /etc/fstab
		
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
	def riak(args = []):
		# Dependencies
		Install.make()
		
		call(["git", "clone", "git://github.com/basho/riak.git"])
		os.chdir("./riak")
		call(["make", "rel"])
		
	def make(args = []):
		call(["sudo", "apt-get", "install", "make"])

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