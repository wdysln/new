metadata = """
summary @ Extended attribute support library for ACL support
homepage @ http://oss.sgi.com/projects/xfs/
license @ LGPL-2
src_url @ http://download.savannah.gnu.org/releases-noredirect/$name/$fullname.src.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""



def install():
    raw_install("DIST_ROOT=%s install install-lib install-dev" % install_dir)
