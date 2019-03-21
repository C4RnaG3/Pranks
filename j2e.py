#!/usr/bin/python

# -*- coding: utf-8 -*-

#-- Used for Jiami to English translation for later use

#-- Basic libraries
import sys, argparse, codecs

#-- Imports the Translator module from the googletrans library (needs to be installed)
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
    print(translation.origin, ' -> ', translation.text)
