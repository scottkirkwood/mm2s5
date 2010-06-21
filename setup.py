#!/usr/bin/env python

from distutils.core import setup
import re

NAME='mm2s5'
VER='0.2.2'
DIR='mm2s5'
PY_NAME=NAME
DEB_NAME=NAME
RELEASE_FILE='CHANGELOG.txt'
RELEASE_FORMAT=r'Version (?P<ver>[^ ]+) \((?P<date>[^)]+)\)'

PY_SRC='%s.py' % PY_NAME
DEPENDS=[]
MENU_SUBSECTION='Utils'
DEPENDS_STR=' '.join(DEPENDS)
AUTHOR_NAME='Scott Kirkwood'
GOOGLE_CODE_EMAIL='scott@forusers.com'
KEYWORDS=['mm', 'S5', 'FreeMind', 'Presentation', 'XML', 'Python']
MAN_FILE='man/%s.1' % NAME
DESKTOP_FILE=None
ICON=None
COMMAND='/usr/bin/%s' % NAME

SETUP = dict(
    name=NAME,
    version=VER,
    packages=[NAME],
    package_dir = {
        NAME: NAME},
    description="Convert a FreeMind mind-map (mm) into an S5 (html) presentation",
    long_description=
"""This is a simple utility to convert a FreeMind mind-map (.mm) into an S5 (html) presentation.  
The root node becomes the start page and each top level node below that becomes a slide.
Lower level nodes become increasingly nested lists.
Images are also supported.
""",
    author='Scott Kirkwood',
    author_email='scott@forusers.com',
    url='http://code.google.com/%s/' % NAME,
    download_url='http://%s.googlecode.com/files/%s-%s.zip' % (NAME, NAME, VER),
    keywords=' '.join(KEYWORDS),
    license='Apache 2.0',
    platforms=['POSIX', 'Windows'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Documentation',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Utilities',
    ], 
    scripts=['scripts/mm2s5'],
)

COPYRIGHT = 'Copyright (C) 2010 %s' % (AUTHOR_NAME) # pylint: disable-msg=W0622
LICENSE_TITLE = 'Apache License'
LICENSE_SHORT = 'Apache'
LICENSE_VERSION = '2.0'
LICENSE_TITLE_AND_VERSION = '%s version %s' % (LICENSE_TITLE, LICENSE_VERSION)
LICENSE = '%s or any later version' % LICENSE_TITLE_AND_VERSION # pylint: disable-msg=W0622
LICENSE_TITLE_AND_VERSION_ABBREV = '%s v%s' % (LICENSE_SHORT, LICENSE_VERSION)
LICENSE_ABBREV = '%s+' % LICENSE_TITLE_AND_VERSION_ABBREV
LICENSE_URL = 'http://www.apache.org/licenses/LICENSE-2.0'
LICENSE_PATH = '/usr/share/common-licenses/Apache-2.0'
LICENSE_NOTICE = '''%(name)s is free software: you can redistribute it and/or modify
it under the terms of the Apache License as published by
the Apache Software Foundation, either version 2 of the License, or
(at your option) any later version.

%(name)s is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the Apache License
along with this program.  If not, see <%(url)s>.''' % dict(name=NAME, url=LICENSE_URL)
LICENSE_NOTICE_HTML = '<p>%s</p>' % LICENSE_NOTICE.replace('\n\n', '</p><p>')
LICENSE_NOTICE_HTML = re.sub(r'<http([^>]*)>', r'<a href="http\1" target="_blank">http\1</a>', LICENSE_NOTICE_HTML)

if __name__ == '__main__':
  setup(**SETUP)
