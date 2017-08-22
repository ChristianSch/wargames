#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <sys/types.h>

uint8_t XORkey = 0x41;
char secret_password[] =  ")q6\036(2\036\065)p2\036)u\"*r3\036'q--q6(/&\036,r";

int main() {
    int i;
    for(i=0; i<strlen(secret_password); i++) {
        secret_password[i] = secret_password[i] ^ XORkey;
    }
    printf("%s\n", secret_password);
    return 0;
}
