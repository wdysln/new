metadata = """
summary @ XML to PO and back again
homepage @ http://itstool.org/
license @ GPL3
src_url @ http://files.itstool.org/$name/$fullname/tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-libs/libxml2
"""

def configure():
    autoreconf("-fi")

def install():
    raw_install("DESTDIR=%s" % install_dir)
