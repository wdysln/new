metadata = """
summary @ An XML parser library
homepage @ http://expat.sourceforge.net
license @ MIT
src_url @ http://downloads.sourceforge.net/sourceforge/expat/expat-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
srcdir ="expat-%s" %version

get("main/lib32_utils")
