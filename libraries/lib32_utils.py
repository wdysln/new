# Copyright 2009 - 2011 Burak Sezer <purak@hadronproject.org>
#
# This file is part of main repository
#
# main repository is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# main repository is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with main repository.  If not, see <http://www.gnu.org/licenses/>.

# lib32-related build operations
import lpms
import os

get("main/fdo_mime", "main/extract_utils")

primary_library = "lib32_utils"

# variable checks
try:
    subdir
except NameError:
    subdir = ""

try:
    source_archive
except NameError:
    source_archive = None

def lib32_utils_extract():
    if source_archive:
        tar_extract("%s" % source_archive)
    else:
        for item in extract_plan:
            tar_extract(lib32-basename(item))

# Functions
def lib32_utils_prepare():
	export('CC="gcc -m32")
	export('CXX="g++ -m32")
	export('PKG_CONFIG_PATH="/usr/lib32/pkgconfig")
	

def lib32_utils_configure():
    conf("--prefix=/usr",
		"--libdir=/usr/lib32")

def lib32_utils_build():
    make()

def lib32_utils_install():
    installd()
	system("rm -rf %s/usr/{bin,include,share}" % install_dir)
	
def lib32_utils_post_install():
    xdg_icon_resource()

