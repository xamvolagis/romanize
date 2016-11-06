#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

# Note: since this is specifically indented for file names,
# injectivity and the use of standard characters (for example, avoiding
# quotation marks) is prioritized oer conformance to standards.

ru_dict = {
  'А': 'A',
  'Б': 'B',
  'В': 'V',
  'Г': 'G',
  'Д': 'D',
  'Е': 'Je',
  'Ё': 'Jo',
  'Ж': 'Zh',
  'З': 'Z',
  'И': 'I',
  'Й': 'Jj',
  'К': 'K',
  'Л': 'L',
  'М': 'M',
  'Н': 'N',
  'О': 'O',
  'П': 'P',
  'Р': 'R',
  'С': 'S',
  'Т': 'T',
  'У': 'U',
  'Ф': 'F',
  'Х': 'X',
  'Ц': 'C',
  'Ч': 'Ch',
  'Ш': 'Sh',
  'Щ': 'Shh',
  'Ъ': 'Jy',
  'Ы': 'Y',
  'Ь': 'Ji',
  'Э': 'E',
  'Ю': 'Ju',
  'Я': 'Ja',
}

def cyr2lat(s):
  return ''.join(ru_dict[c] if 1039 < ord(c) <= 1071 else
                 ru_dict[c.upper()].lower() if 1071 < ord(c) < 1104 else
                 c
                 for c in s)

def main():
  parser = argparse.ArgumentParser(description='Romanize (a) file name(s).')
  parser.add_argument('name', metavar='N', type=str)
  args = parser.parse_args()

  cwd = os.getcwd()
  name = args.name
  # Remove spaces.
  name = name.replace(' ', '_')

  name = cyr2lat(name)

  if os.path.exists(os.path.join(cwd, args.name)):
    os.rename(os.path.join(cwd, args.name),
              os.path.join(cwd, name))

if __name__ == '__main__':
  main()
