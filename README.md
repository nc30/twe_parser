# TWE Parser

## over view

this module is TWE-Lite(http://mono-wireless.com/jp/products/TWE-Lite-DIP/index.html) s Serial responce Parther


## example

~~~

import twe_parser

code = b':7881150175810000380026C9000C04220000FFFFFFFFFFA7'
responce = twe_parser.parse( code )

print( responce.DIN )

~~~

