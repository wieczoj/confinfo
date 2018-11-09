# Common interface for editing files.
# (C) 2018-11 Janusz Wieczorek <wieczoj@gmail.com>

#    This package is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 dated June, 1991.

#    This package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    For a copy of the GNU General Public License,
#    write to the Free Software Foundation, Inc.,
#    51 Franklin St, Fifth Floor, Boston, MA
#    02110-1301 USA

import re
import os
from pathlib import Path

from subprocess import call


class Confinfo():
    """some configuration files"""
    def __init__(self, name):
        self.name = name

    def info(self):
        print('The configuration file does not exist.')
        exit(2)

    def showversion(self):
        files = ['/proc/version', self.name]
        for f in files:
            with open(f) as file_object:
                content = file_object.read()
                print(content)

    def etcmtab(self, flaga = 0):
        """content of the /etc/mtab   default only real storage   etcmtab(1) -> full content"""
        p = re.compile('^/')
        path = '/etc/mtab'
        file = Path(path)
        if not file.is_file():
            self.info()
        with open(path) as file_object:
            for line in file_object:
                if flaga == 0:
                    if p.match(line):
                        print(line)
                else:
                    print(line)

    def etcfstab(self, flaga = 0):
        """content of the /etc/fstab   default only real storage   etcmfstab(1) -> full content"""
        p = re.compile('[^#]')
        path = '/etc/fstab'
        file = Path(path)
        if not file.is_file():
            self.info()
        if flaga == 2:
            edytor = os.environ["EDITOR"]
            call([edytor, path])
        else:
            with open(path) as file_object:
                for line in file_object:
                    if flaga == 0:
                        if p.match(line):
                            if line.strip():
                                print(line)
                    else:
                        if line.strip():
                            print(line)

    def etcnetworkinterfaces(self, flaga = 0):
        """content of the /etc/network/interfaces   default only real storage  """
        p = re.compile('[^#]')
        path = '/etc/network/interfaces'
        file = Path(path)
        if not file.is_file():
            self.info()

        if flaga == 2:
            edytor = os.environ["EDITOR"]
            call([edytor, path])
        else:
            with open(path) as file_object:
                for line in file_object:
                    if flaga == 0:
                        if p.match(line):
                            if line.strip():
                                print(line)
                    else:
                        if line.strip():
                            print(line)