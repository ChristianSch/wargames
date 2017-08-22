#!/bin/bash
# encrypts password files.
# `passwd.public` files are encrypted and written to `passwd.secret`,
# the public file is then removed.
EMAIL="SECRET"
IN="passwds.public"
OUT="passwds.secret"

for basePath in $(find . -name $IN | sed "s/\.\/\(.*\)$IN/\1/"); do
    echo $basePath$IN "to" $basePath$OUT
    gpg --output $basePath$OUT --encrypt --user $EMAIL --yes $basePath$IN \
        && test -e $basePath$OUT \
        && rm $basePath"passwds.public" \
        && echo " << pruned"
done

