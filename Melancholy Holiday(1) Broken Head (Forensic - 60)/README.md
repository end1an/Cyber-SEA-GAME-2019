# Melancholy Holiday(1) Broken Head (Forensic - 60) 
The challenge gives us a zip file that we couldn't to unzip because the header file format is missing or broken.

```
$ unzip Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip
Archive:  Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip
file #1:  bad zipfile offset (local header sig):  0
```

So, we used the vim + xxd to view the hex of the broken-zip file.

```
$ vim Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip

/** Switching to the hex mode, and you can patching the binary file **/
:%!xxd

As you can see, there are the dead beef at the top of file.

00000000: dead beef 1400 0000 0000 e951 4f4d fd1b  ...........QOM..
00000010: 97f7 225e 0400 769f 0500 551f 0000 696d  .."^..v...U...im
00000020: 706f 7274 616e 742e 626d 7054 99d7 72e3  portant.bmpT..r.
00000030: 3614 862d 9144 0708 5691 1445 754b 966b  6..-.D..V..EuK.k
00000040: acac bde9 bdf7 36e9 7592 496e 3293 8b4c  ......6.u.In2..L

We change "dead beef" byte to the zip magic number "504b 0304."

00000000: 504b 0304 1400 0000 0000 e951 4f4d fd1b  ...........QOM..
00000010: 97f7 225e 0400 769f 0500 551f 0000 696d  .."^..v...U...im
00000020: 706f 7274 616e 742e 626d 7054 99d7 72e3  portant.bmpT..r.
00000030: 3614 862d 9144 0708 5691 1445 754b 966b  6..-.D..V..EuK.k
00000040: acac bde9 bdf7 36e9 7592 496e 3293 8b4c  ......6.u.In2..L

/** To save the patching, you have to switch back to normal mode **/
:%!xxd -r
:wq
```

After patching, we unzip the file again. There are the file name important.bmp inside the zip file.
However, we can't unzip it because some of error below.

```
$ unzip Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip
Archive:  Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip
warning:  filename too long--truncating.
[ important.bmpT��r�6^T�-�D^G^HV�^TEuK�k���ڢ�6�u�In2��L�$�yi� ]
important.bmp:  mismatching "local" filename (important.bmpT��r�6^T�-�D^G^HV�^TEuK�k���ڢ�6�u�In2��L�$�yi�),
         continuing with "central" filename version
important.bmp:  ucsize 368502 <> csize 286242 for STORED entry
         continuing with "compressed" size value
 extracting: important.bmp            bad CRC dac4babb  (should be f7971bfd)
```

Let check the zip file by using zipdetails command. As you can see, the value of "Filename Length" is equal to "1F55" (8021) that is not correct length of the file important.bmp.

```
$ zipdetails -v Broken_Head_365a1c80b6ac1c5b908a3fa2526a3535320684e1.zip | less

00000 00004 50 4B 03 04 LOCAL HEADER #1       04034B50
00004 00001 14          Extract Zip Spec      14 '2.0'
00005 00001 00          Extract OS            00 'MS-DOS'
00006 00002 00 00       General Purpose Flag  0000
00008 00002 00 00       Compression Method    0000 'Stored'
0000A 00004 E9 51 4F 4D Last Mod Time         4D4F51E9 'Mon Oct 15 10:15:18 2018'
0000E 00004 FD 1B 97 F7 CRC                   F7971BFD
00012 00004 22 5E 04 00 Compressed Length     00045E22
00016 00004 76 9F 05 00 Uncompressed Length   00059F76
0001A 00002 55 1F       Filename Length       1F55
0001C 00002 00 00       Extra Length          0000
page overflow at /usr/bin/zipdetails5.18 line 354.
0001E 01F55 69 6D 70 6F Filename              'important.bmpT<99><D7>r<E3>6 <86>-
            72 74 61 6E                       <91>D  V<91> EuK<96>k<AC><AC><BD><E9><BD><F7>6<E9>u<92>In2<93><8B>L<9E>$<F7>y<D5><FC>
            74 2E 62 6D                       R<B9><C7>g Qi.><FC> <F4><F3>o<F
```
