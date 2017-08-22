#!/bin/bash
# decrypts password files.
# level passwords are written as clear text into `passwds.public`
# in their respective directory.
EMAIL="SECRET"
IN="passwds.secret"
OUT="passwds.public"

for basePath in $(find . -name "passwds.secret" | sed "s/\.\/\(.*\)$IN/\1/"); do
    echo $basePath$IN "to" $basePath$OUT
    gpg --output $basePath$OUT --yes --decrypt $basePath$IN \
        && echo " >> made visible"
done
