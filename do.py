#!/usr/bin/env python3

# Imports
from subprocess import call

# ls
call(["ls", "-la", "--color"])

# Riak
riakUrl = "http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.5/ubuntu/trusty/riak_2.0.5-1_amd64.deb"