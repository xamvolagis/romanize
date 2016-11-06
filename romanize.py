#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

# Note: since this is specifically indented for file names,
# injectivity and the use of standard characters (for example, avoiding
# quotation marks) is prioritized oer conformance to standards.

ru_dict = {
  u'А': u'A',
  u'Б': u'B',
  u'В': u'V',
  u'Г': u'G',
  u'Д': u'D',
  u'Е': u'Je',
  u'Ё': u'Jo',
  u'Ж': u'Zh',
  u'З': u'Z',
  u'И': u'I',
  u'Й': u'Jj',
  u'К': u'K',
  u'Л': u'L',
  u'М': u'M',
  u'Н': u'N',
  u'О': u'O',
  u'П': u'P',
  u'Р': u'R',
  u'С': u'S',
  u'Т': u'T',
  u'У': u'U',
  u'Ф': u'F',
  u'Х': u'X',
  u'Ц': u'C',
  u'Ч': u'Ch',
  u'Ш': u'Sh',
  u'Щ': u'Shh',
  u'Ъ': u'Jy',
  u'Ы': u'Y',
  u'Ь': u'Ji',
  u'Э': u'E',
  u' ' : '_',
}

def cyr2lat(s):
  return ''.join(ru_dict[c] if ord(c) < 1072 else ru_dict[c.upper()].lower()
                 for c in s)

def main():
  parser = argparse.ArgumentParser(description='Romanize (a) file name(s).')
  parser.add_argument('name', metavar='N', type=str)
  args = parser.parse_args()

  cwd = os.getcwd()
  if os.path.exists(os.path.join(cwd, args.name)):
    os.rename(os.path.join(cwd, args.name),
              os.path.join(cwd, cyr2lat(args.name)))

if __name__ == '__main__':
  main()
