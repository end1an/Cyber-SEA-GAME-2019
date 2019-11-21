Download the execution file [here](RLO_7904ba4cdb3b1cb4c6a9f767c9ef065c.exe).  

After running the file on windows, it extraced a lot of blank files.  
_Please notice that the output from `dir` command was sorted by time._  
```
C:\Users\admin\Desktop\RLO_7904ba4cdb3b1cb4c6a9f767c9ef065c>dir /O:D
 Volume in drive C has no label.
 Volume Serial Number is C68E-9F89

 Directory of C:\Users\admin\Desktop\RLO_7904ba4cdb3b1cb4c6a9f767c9ef065c

11/21/2019  04:18 PM    <DIR>          ..
11/21/2019  04:18 PM    <DIR>          .
12/31/2019  10:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcde?_{}zyxwvutsrqponmlkjihgf
12/31/2019  11:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk?_{}zyxwvutsrqponml
01/01/2020  12:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZ?_{}zyxwvutsrqponmlkjihgfedcba
01/01/2020  01:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef?_{}zyxwvutsrqponmlkjihg
01/01/2020  02:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{?_{
01/01/2020  03:00 AM                 0 ABCDEFGHIJKLMNOPQ?_{}zyxwvutsrqponmlkjihgfedcbaZYXWVUTSR
01/01/2020  04:00 AM                 0 ABCDEFGHIJK?_{}zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONML
01/01/2020  05:00 AM                 0 ABCDEFGHIJKLMN?_{}zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPO
01/01/2020  06:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}?_
01/01/2020  07:00 AM                 0 ABC?_{}zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFED
01/01/2020  08:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh?_{}zyxwvutsrqponmlkji
01/01/2020  09:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr?_{}zyxwvuts
01/01/2020  10:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopq?_{}zyxwvutsr
01/01/2020  11:00 AM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst?_{}zyxwvu
01/01/2020  12:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmno?_{}zyxwvutsrqp
01/01/2020  01:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs?_{}zyxwvut
01/01/2020  02:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}?_
01/01/2020  03:00 PM                 0 ABCDEFGHIJKLMNOPQRST?_{}zyxwvutsrqponmlkjihgfedcbaZYXWVU
01/01/2020  04:00 PM                 0 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?_{}
              19 File(s)              0 bytes
               2 Dir(s)  42,757,038,080 bytes free
```
Assume the the original list of chracters  **ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_{}**  
The flag is the missing character before "?_" of each file which ordered by time.  
For example, The first character of the flag is the character after "e" (ABCDEFGHIJKLMNOPQRSTUVWXYZabcde****?_****{}zyxwvutsrqponmlkjihgf) which is "f".  
The second character of the flag is the character after "k" (ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk****?_****{}zyxwvutsrqponml) which is "l".  

The flag is flag{RLO_Disrupt_U}


