#!/usr/bin/python

# -*- coding: utf-8 -*-


# Tested against a file copied from https://hotexamples.com/examples/-/-/jiami/php-jiami-function-examples.html

#-- Basic libraries
import sys, argparse

#-- Imports the Translator module from the googletrans library (needs to be installed -- pip install googletrans)
from googletrans import Translator

#----------------------
#-- Command line parsing
parser = argparse.ArgumentParser(prog='j2e')
parser.add_argument('--file', help='File for parsing')
args = parser.parse_args()
#----------------------
#-- File reading... if you can tell, I'm not good at python lol
f=open(sys.argv[2], 'r')
jfile=f.read()

#-- intializes translator
translator = Translator(service_urls=['translate.google.com'])

#-- https://github.com/ssut/py-googletrans/blob/master/googletrans/constants.py

translations = translator.translate([jfile], dest='en')
for translation in translations:
#-- translates the unicode to its English equivelant
#-- Cleaned up the output, will display the whole decoded file, with some unneded capitalization
    print("Translation: ")
    print(translation.text)
    
