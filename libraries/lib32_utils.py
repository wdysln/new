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


import lpms

def lib32_conf(*parameters, **kwargs):
    append_cflags("-O2 -g -m32")
    append_cxxflags("-O2 -g -m32")
    append_ldflags("-O2 -g -m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
       
    conf_command = './configure \
                     --prefix=/usr \
                    --mandir=/tmp32 \
                    --infodir=/tmp32 \
                    --datadir=/tmp32 \
                    --bindir=/tmp32 \
                    --sbindir=/tmp32 \
                    --sysconfdir=/tmp32 \
                    --docdir=/tmp32 \
                    --localedir=/tmp32 \
                    --localstatedir=/tmp32 \
                    --libexecdir=/usr/lib32 \
                    --libdir=/usr/lib32'
                    
    args_pretty = conf_command+" "+"\n\t".join(parameters)
    out.notify("running %s" % args_pretty)
    if "run_dir" in kwargs:
        conf_command = os.path.join(kwargs["run_dir"], "configure")

    if not system("%s %s" % (conf_command, " ".join(parameters))):
        raise BuildError("lib32 configure failed.")


def lib32_utils_configure():
    lib32_conf()

def lib32_utils_build():
    make()

def lib32_utils_install():
    raw_install("DESTDIR=%s" % install_dir)
    rmdir("/tmp32")
    if isdir("/usr/include"):
       rmdir("/usr/include")




