metadata = """
summary @ A cross-platform open softwre make system
homepage @ http://www.cmake.org
license @ CMake
src_url @ http://www.cmake.org/files/v3.3/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/expat app-arch/libarchive net-misc/curl
          x11-misc/shared-mime-info 
"""

def configure():
    system("./bootstrap --prefix=/usr \
            --mandir=/share/man \
            --docdir=/share/doc/cmake \
             --no-system-jsoncpp \
            --system-libs \
            --parallel=2")

def install():
    raw_install("DESTDIR=%s" % install_dir)
