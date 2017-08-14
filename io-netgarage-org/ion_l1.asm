; ...
.main:
    ; <main+3>
    add    al,0x8
    ; <main+5>
    call   0x804810f ; 0x8048085 (print)
    ; <main+10>
    call   0x804809f ; 0x804808a (scanf)
    ;  <main+15>
    ; compare eax to 0x10f = 16^2 + 0* 16^1 + 15 = 271
    ; ^ f = 15
    cmp    eax,0x10f ; 0x804808f
    ; <main+20>
    je     0x80480dc ; 0x8048094
    ; <main+26>
    call   0x8048103 ; 0x804809a (exit)

.puts: ; 0x804810f
    ; EAX: msg
    mov    eax,0x4 ; sys_write
    mov    ebx,0x1 ; to stdout
    mov    edx,0x25 ; print first 37 chars of "msg"
    int    0x80 ; interrupt
    ; EAX is now 0x25, the number of written chars/bytes

.fscanf: ; 0x804809f
    ; call fscanf, gets read into ecx
    mov    eax,0x3
    mov    ebx,0x0
    mov    ecx,esp
    mov    edx,0x1000
    int    0x80

    ; call skipwhite


.skipwhite:
    lods   al,BYTE PTR ds:[esi] ; put first char of input into AL
    ; EAX: first char, ECX: full input, ESI: remaining input, ESP: full input
    cmp    al,0x20 ; is space?
    je     0x80480bc
    ; checks if input is above 0x39
    ; [41,5A] is upper case A-Z
    ; [61,7A] is lower case a-z
    sub    al,0x30
    cmp    al,0x9
    ja     0x80480d3

    ; doit/exitscanf
    mov    eax,ebx ; (ebx = 0x0)
    add    esp,0x1000
    ret

.exit:
    mov    eax,0x1
    mov    ebx,0x0
    int    0x80

.data:
; msg: ("Enter the 3 digit passcode to enter: Congrats you found it, now read the password for level2 from /home/level2/.pass\n/bin/sh")

; level 1: 271
; level 2: XNWFtWKWHhaaXoKI

