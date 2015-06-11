metadata = """
summary @ An event notification library
homepage @ http://www.monkey.org/~provos/libevent/
license @ GPL2
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/libevent/libevent-2.0.21-stable.tar.gz/b2405cc9ebf264aa47ff615d9de527a2/libevent-$version-stable.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl
"""

srcdir = name+"-"+version+"-stable"

def install():
    raw_install("DESTDIR=%s" % install_dir)
