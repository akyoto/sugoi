#!/usr/bin/env python3

# Imports
import subprocess
import sys
import os

call = subprocess.call
Popen = subprocess.Popen

# Commands
class Commands:
	def blockport(args):
		if not args:
			print("Syntax: blockport YOUR_PORT_NUMBER")
			return
		
		call(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", args[0], "-s", "127.0.0.1", "-j", "ACCEPT")
		call(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", args[0], "-j", "DROP")
	
	def diskspace(args):
		call(["df", "-h", "-x", "tmpfs"] + args)
	
	def info(args):
		call(["uname", "-a"] + args)
		
	def ls(args):
		call(["ls", "-la", "--color"] + args)
		
	def memory(args):
		def showMemory(grepString):
			meminfo = Popen(["cat", "/proc/meminfo"], stdout = subprocess.PIPE)
			grep = Popen(["grep", grepString], stdin = meminfo.stdout, stdout = subprocess.PIPE)
			sys.stdout.write(grep.communicate()[0].decode("utf-8"))
		
		showMemory("Mem")
		showMemory("Buffers")
		showMemory("Cached")
		
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
		
	def update(args):
		call(["sudo", "apt-get", "update"])
		call(["sudo", "apt-get", "upgrade"])
		
	def uptime(args):
		print("\nUptime:")
		call(["uptime"] + args)
		
	def install(args):
		vars(Install)[args[0]](args[1:])
		
	def __getitem__(self, name):
		return getattr(self, name)

# Package installations
class Install:
	def make(args = []):
		call(["sudo", "apt-get", "install", "make"])
	
	def riak(args = []):
		# Dependencies
		Install.make()
		
		call(["git", "clone", "git://github.com/basho/riak.git"])
		os.chdir("./riak")
		call(["make", "rel"])
		
		# TODO: Switch to binary download

# Help
def showHelp():
	print("Commands:")
	
	for cmd in vars(Commands):
		if cmd[0] == "_":
			continue
		
		print("\t" + cmd)

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
