metadata = """
summary @ A utility to apply patch files to original sources
homepage @ http://www.gnu.org/software/patch/patch.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ static
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""


def build():
    if opt('static'):
        append-ldflags('-static')
    make()
