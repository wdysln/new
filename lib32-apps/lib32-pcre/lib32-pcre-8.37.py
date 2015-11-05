metadata = """
summary @ A library that implements Perl 5-style regular expressions
homepage @ http://www.pcre.org
license @ BSD
src_url @ ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-$version.tar.bz2
arch @ ~x86_64
"""

srcdir = "pcre-%s" %version

get("main/lib32_utils")



def configure():
    lib32_conf("--enable-utf8",
        "--enable-pcre16",
        "--enable-pcre32",
        "--enable-jit",
        "--enable-unicode-properties")

def build():
    append_cflags("-fPIC")
    make()


def install():
    raw_install("DESTDIR=%s" % install_dir)
    rmdir("/tmp32")
    rmdir("/usr/include")