metadata = """
summary @ XML-XCB protocol descriptions
homepage @ http://xcb.freedesktop.org/
license @ custom
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python:2.7 dev-libs/libxml2
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
