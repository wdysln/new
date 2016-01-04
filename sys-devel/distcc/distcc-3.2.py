metadata = """
summary @ Handy console-based calculator utility
homepage @ http://www.gnu.org/software/bc/bc.html
license @ GPL-2 LGPL-2.1
src_url @ http://distcc.googlecode.com/files/$fullnamerc1.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ sys-devel/flex
"""
srcdir = "distcc-3.2rc1"

def configure():
    conf("--disable-Werror")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    for i in ["cc", "gcc","g++", "c++","cpp"]:
        makesym("/usr/bin/distcc", "/usr/lib/distcc/bin/%s"% i)
  #  insdoc("AUTHORS", "FAQ", "NEWS", "README", "ChangeLog")
    insfile("%s/distccd" % filesdir, "/etc/conf.d/distccd")
    insfile("%s/distccd.service" % filesdir, "/usr/lib/systemd/system/distccd.service")