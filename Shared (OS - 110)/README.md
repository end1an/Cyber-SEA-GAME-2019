# Shared (OS - 110)

The challenge file can be download (here)[Shared_04dca129c011213979aded2e7bef71d3.zip].
  
After extracting the ZIP file, there are 2 files, `main.exe` and `libflag.so`.  
```
$ file *
libflag.so: ELF 64-bit LSB shared object x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=faf5c5024cf5540c401aaaa188e6a1dc5374964c, not stripped
main.exe:   ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.18, BuildID[sha1]=572e5a45a57b8e8de469cfe301e7d653fb4a6565, not stripped
```
By running the `main.exe`, the error was occured.  
Then use command `strace ./main.exe` to see what library called.  
The result showed that a lot of `libflag.so` files from different multiple directories were called but they were missing.  
!(strace)[strace.png]
  
So I copied the `libflag.so` to all required directory, and run `main.exe` again.  
!(flag)[flag.png]


