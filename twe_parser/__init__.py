#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
にとりかわいい - Nitori is Pritty -
'''


__version__ = '0.1.0'
__author__  = 'Asahi Himura <himura@nitolab.com>'
__date__    = '13/2/2016'
__license__ = "MIT"


from .twe_responce import TWE_Responce

def parse( string ):
	return TWE_Responce( string )
