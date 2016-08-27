# Sugoi
Swiss army knife for linux.

## Installation

```
./sugoi install sugoi
```

Add `alias s='sugoi'` in your `.bash_aliases` for more awesomeness.

## Usage

```
~$ s
Commands:
	addKeyToServer
	blockPort
	clearFirewall
	cpu
	cpuUsage
	diskUsage
	disks
	downloadFromServer
	freeMemory
	help
	install
	ls
	memory
	memoryUsage
	os
	processCount
	push
	redirectPort
	stats
	tcp
	tcpCount
	tune
	udp
	udpCount
	update
	upgrade
	uptime
	usage
```

## Examples

### git add + git commit + git push
```
~$ s push "Changed some stuff"
```
I personally use `alias sp='sugoi push'` to type it even faster.

### Add SSH key to remote server
```
~$ s addKeyToServer admin@github.com
```

Enables SSH auto-login for the specified server. Key needs to be stored in `~/.ssh/id_rsa.pub`.

### Download file from server
```
~$ s downloadFromServer admin@github.com /home/admin/database.dat
```

Downloads starts instantaneously if you added your SSH key to the server.

### Redirect port
```
~$ s redirectPort 80 4000
~$ s redirectPort 443 4001
```

### Block a port
```
~$ s blockport 3000
```

### Clear firewall rules
```
~$ s clearFirewall
```


### Show resource usage
```
~$ s usage
CPU usage:          3%
Memory usage:       34%
Disk usage:         73%
```