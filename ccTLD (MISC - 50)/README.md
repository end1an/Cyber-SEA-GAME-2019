# ccTLD (MISC - 50)
To solve this challenge we have to fill the ● | ■ to get the flag.  
Flag format is flag{A_B} Ex. flag{au_c3lkbmV5}  

This challenge provided us the following data.

```
A | B
au | c3lkbmV5
us | dWNudi1uY21nLWVrdmE=
gr | ZXhsaXJ3
it | emF4b3Q=
cn | am1xcnF2bw==
ca | Zmt4bXllZm9i
gb | eGF6cGF6
ru | Z2Nxdnc=
br | aHll
kr | aHF3Z2Z5dXpzZnk=
● | ■
cn | eGFlZmVqYw==
fr | bnlwZ3E=
it | Z2NsdWhp
us | bmM=
```

Column A looks like a country abbreviation and column B seems to be Base64 encoding of something. 
Then tried to Base64 decode the data but we got only the city name for au.

```
A | B
au | sydney
us | ucnv-ncmg-ekva
gr | exlirw
it | zaxot
cn | jmqrqvo
ca | fkxmyefob
gb | xazpaz
ru | gcqvw
br | hye
kr | hqwgfyuzsfy
● | ■
cn | xaefejc
fr | nypgq
it | gcluhi
us | nc
```

Tried to decrypt it with ROT Cipher with -2 -4 -6 ... and got all the country names.

```
A | B
au | sydney
us | salt-lake-city     //-2
gr | athens             //-4
it | turin              //-6
cn | beijing            //-8
ca | vancouver          //-10
gb | london             //-12
ru | sochi              //-14
br | rio                //-16
kr | pyeongchang        //-18
● | ■
cn | beijing            //-22
fr | paris              //-24
it | gcluhi             //-26
us | la                 //-28
```
These look like the list of Olympic host cities.

- 2000  Sydney, Australia
- 2004  Athens, Greece
- 2008  Beijing, China
- 2012  London, England
- 2016  Rio de Janeiro, Brazil
- 2020  Tokyo, Japan
- 2024  Paris, France
- 2028  Los Angeles, United States

The "● | ■" must be "jp | tokyo".
We encrypted "tokyo" with ROT20 and then encoded with Base64.
```
jp | bmllc2k=
```
Finally the flag is flag{jp_bmllc2k=}