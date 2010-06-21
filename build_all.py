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

import os
import sys
import re
from pybdist import pybdist
import setup

if __name__ == '__main__':
  import optparse
  parser = optparse.OptionParser()
  parser.add_option('--clean', dest='doclean', action='store_true',
                    help='Uninstall things')
  parser.add_option('--dist', dest='dist', action='store_true',
                    help='Only build distributions.')
  parser.add_option('--upload', dest='upload', action='store_true',
                    help='Only upload to google code.')
  parser.add_option('--pypi', dest='pypi', action='store_true',
                    help='Only upload to pypi')
  parser.add_option('--freshmeat', dest='freshmeat', action='store_true',
                    help='Announce on freshmeat')
  parser.add_option('--twitter', dest='twitter', action='store_true',
                    help='Announce on twitter')
  parser.add_option('--all', dest='all', action='store_true',
                    help='Do everything')
  (options, args) = parser.parse_args()
  ver = pybdist.GetVersion(setup)
  rel_date, rel_lines = pybdist.ParseLastRelease(setup)
  print 'Version is %r, date %r' % (ver, rel_date)
  print 'Release notes'
  print '-------------'
  print '\n'.join(rel_lines)
  print

  if options.doclean:
    pybdist.CleanAll(setup)
  elif options.dist:
    pybdist.BuildMan(setup)
    pybdist.BuildZipTar(setup)
    pybdist.BuildDeb(setup)
  elif options.upload:
    pybdist.UploadToGoogleCode(setup)
  elif options.pypi:
    pybdist.UploadToPyPi(setup)
  elif options.freshmeat:
    pybdist.AnnounceOnFreshmeat(setup)
  elif options.twitter:
    pybdist.AnnounceOnTwitter(setup)
  elif options.all:
    pybdist.BuildMan(setup)
    pybdist.BuildZipTar(setup)
    pybdist.BuildDeb(setup)
    pybdist.UploadToGoogleCode(setup)
    pybdist.UploadToPyPi(setup)
    pybdist.AnnounceOnFreshmeat(setup)
    pybdist.AnnounceOnTwitter(setup)
  else:
    print 'Doing nothing.  --help for commands.'
