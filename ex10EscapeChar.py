#Escape Sequences

# print(
# \n '\\ continuation character'
# \n \'  
# \n\" 
# \n '\a  ASCII bell (BEL)'
# \n\b 'backspace' 
# \n\f 'ascii formfeed(FF)'
# \n \n 'linefeed (LF)'
# \n \N{name} 'Chracter named name (Unicode oly)'
# \n \r 'ASCII carriage return (CR)'
# \n\t 'ASCII horizontal tab'
# \n\uxxxx 'ASCII 16-bit hex (Unicode only)'
# \n\Uxxxxxxxx 'ASCII32-bit hex (Unicode only)'
# \n \v 'ASCII Vertical tab'
# \n\ooo 'Character with octal value oo'
# \n\xhh  'Character with hex valie hh'
# )

while True:
  for i in ["/","-","|","\\","|"]:
    print ("%s\r" % i)
