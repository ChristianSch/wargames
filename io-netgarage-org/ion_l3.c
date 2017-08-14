//bla, based on work by beach

#include <stdio.h>
#include <string.h>

// 0x08048474
void good()
{
        puts("Win.");
        execl("/bin/sh", "sh", NULL);
}
void bad()
{
        printf("I'm so sorry, you're at %p and you want to be at %p\n", bad, good);
}

int main(int argc, char **argv, char **envp)
{
        void (*functionpointer)(void) = bad;
        char buffer[50];

        if(argc != 2 || strlen(argv[1]) < 4)
                return 0;

        // copies n bytes (length of string) from
        // argv to buffer
        memcpy(buffer, argv[1], strlen(argv[1]));
        // writes n bytes of value 0 to the buffer
        memset(buffer, 0, strlen(argv[1]) - 4);

        printf("This is exciting we're going to %p\n", functionpointer);
        functionpointer();

        return 0;
}

