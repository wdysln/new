metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ http://ftp.kernel.org/pub/linux/utils/$name/v2.27/$fullname.tar.xz
arch @ ~x86_64
"""

# TODO:
# * Dependencies 
# * Options
# * More configuration
"""
def prepare():
    patch(level=1)
"""   
def configure():
	
    raw_configure("--prefix=/usr",
              "--libdir=/usr/lib",
              "--localstatedir=/run",
              "--enable-fs-paths-extra=/usr/bin:/usr/sbin",
              "--enable-raw",
              "--disable-vipw",
              "--disable-newgrp",
              "--disable-chfn-chsh",
              "--disable-login",
              "--disable-kill",
              "--enable-write",
              "--with-python",
              "--enable-mesg",
              "--enable-socket-activation")
              
def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insfile("%s/uuidd.tmpfiles" % filesdir, "/usr/lib/tmpfiles.d/uuidd.conf")
    insdoc("AUTHORS", "NEWS", "README*")
  

