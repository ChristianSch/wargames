//a little fun brought to you by bla

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <limits.h>

void catcher(int a)
{
//    setresuid(geteuid(),geteuid(),geteuid());
    printf("WIN!\n");
    system("/bin/sh");
    exit(0);
}

int main(int argc, char **argv)
{
    printf("MAX INT: %ld\n",LONG_MAX);
    printf("MIN INT: %ld\n",LONG_MIN);
    puts("source code is available in level02.c\n");
    printf("%d\n", argc);
    printf("%d\n", atoi(argv[2]));

    if (argc != 3 || !atoi(argv[2]))
            return 1;

    printf("checking\n");

    // handle signal SIGFPE, handler is catcher
    signal(SIGFPE, catcher);

    // -2147483648 / -1 = 2147483648
    // which is INT_MAX * 1, hence overflow
    printf("%d\n", abs(atoi(argv[1])) / atoi(argv[2]));
    return abs(atoi(argv[1])) / atoi(argv[2]);
}
