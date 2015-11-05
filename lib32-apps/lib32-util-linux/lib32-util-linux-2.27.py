metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ http://ftp.kernel.org/pub/linux/utils/util-linux/v2.26/util-linux-$version.tar.xz
arch @ ~x86_64
"""


srcdir = "util-linux-%s" %version


standard_procedure = False

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    append_cflags("-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64")
    
def configure():
    flags()
    autoreconf("-fi")
    raw_configure("--libdir=/usr/lib32 \
                     --without-ncurses \
                     --disable-static \
                     --disable-partx \
                     --disable-raw \
                     --disable-write \
                     --disable-mount \
                     --disable-fsck \
                     --without-audit \
                     --without-ncurses \
                     --disable-static \
                     --disable-partx \
                     --disable-raw \
                     --disable-write \
                     --disable-mount \
                     --disable-fsck \
                    --disable-silent-rules \
                    --disable-use-tty-group \
                    --disable-su  \
                    --disable-last \
                    --disable-mesg \
                    --disable-vipw \
                    --disable-wall \
                    --disable-login \
                    --disable-newgrp \
                    --disable-nologin \
                    --disable-runuser \
                    --disable-sulogin \
                    --disable-utmpdump \
                    --disable-chfn-chsh \
                    --disable-mountpoint \
                     --without-systemd \
                    --disable-makeinstall-chown \
                     --disable-libmount")
              
def build():
    flags()
    make()

              
def install():
    flags()
    raw_install("DESTDIR=%s install" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,lib,share,sbin}"% install_dir)
    rmdir("/bin")
    rmdir("/sbin")
        

  

