#!/usr/bin/python

#-- Used for Jiami to English translation for later use
#-- Really early stages

import sys, getopt

#-- Imports the Translator module from the googletrans library (needs to be installed)
from googletrans import Translator

#-- intializes translator
translator = Translator(service_urls=['translate.google.com'])

#-- To do:
#-- file parsing
#-- Wrap this in a loop to continuously translate
#-- Unicode support

#-- https://github.com/ssut/py-googletrans/blob/master/googletrans/constants.py
translations = translator.translate(['hi'], dest='zh-cn')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
    
