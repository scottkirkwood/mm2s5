#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 Scott Kirkwood. All Rights Reserved.
"""
Build everything for mm2s5.

You'll need:
sudo apt-get install alien help2man fakeroot lintian
Also python-bdist
"""

from pybdist import pybdist
import optparse
import setup

def main():
  parser = optparse.OptionParser()
  pybdist.add_standard_options(parser)
  (options, unused_args) = parser.parse_args()

  if not pybdist.handle_standard_options(options, setup):
    print 'Doing nothing.  --help for commands.'

if __name__ == '__main__':
  main()
