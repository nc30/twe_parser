#! /usr/bin/env python3


import tweparse

code = b':0F8115014E81012CFB008268000BDB170101FFFFFFFFFF7F\r\n'
responce = tweparse.parse( code )


