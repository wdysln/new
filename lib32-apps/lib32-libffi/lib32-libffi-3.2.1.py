metadata = """
summary @ A portable, high level programming interface to various calling conventions.
homepage @ http://sourceware.org/libffi
license @ MIT
src_url @ ftp://sourceware.org/pub/libffi/libffi-$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""
srcdir = "libffi-%s" %version


get("main/lib32_utils")
