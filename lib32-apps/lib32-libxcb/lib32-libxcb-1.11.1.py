metadata = """
summary @ X11 client-side library
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/libxcb-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXdmcp x11-libs/libXau
          >=x11-proto/xcb-proto-1.7
build @ dev-util/pkg-config dev-libs/libxslt dev-lang/python:2.7 lib32-apps/lib32-libXau
"""
get("main/lib32_utils")

srcdir = "libxcb-%s" %version

prepare = lambda: patch()



def configure():
    lib32_conf("--enable-xinput")


    
