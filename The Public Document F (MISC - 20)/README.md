# The Public Document F (MISC - 20)

The file was missing.  
  
The challenge is a PDF file. After opening the file, I saw 2 lines of flag but they was blocked with the black block.  
It was found that the first flag is an image which can be obtained by right click and save as image.  
The first flag looked like this <b>flag{dog_*ast;*ast;*ast;*ast;*ast;_*ast;*ast;*ast;*ast;*ast;}</b>. Now I can presume that there are 3 parts of the flag.  
  
The second part of the flag is just the text which can be copied outside the PDF.  
The second part of the flag looked like this <b>flag{*ast;*ast;*ast;*ast;*ast;_monkey_*ast;*ast;*ast;*ast;*ast;}</b>.  
  
The last part of the flag is in the metadata of the PDF which can be seen by running command `exiftool challenge.pdf`.  
  
The flag is flag{dog_monkey_grandpa}
