1. extract zip `fs0ciety.zip` with password `hackthebox`
2. crack password of `fsociety.zip`:
```
zip2john fsociety.zip
john -wordlist=~/wordlists/john.txt zip_hash.txt
```

yields `justdoit`. extract zip.
3. the file contains some weird "encrypted strings":
```
echo $string | base64 -D > out.bin
```
which gives binary outputs as strings with bytes delimited by spaces.
4. get ascii:
```
cat out.bin |  perl -lape '$_=pack"(B8)*",@F' > pass
```
5. done
