metadata = """
summary @ Boost Libraries for C++
homepage @ http://www.boost.org/
license @ Boost-1.0
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name_1_59_0.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-libs/icu dev-lang/python:2.7 app-arch/bzip2 sys-libs/zlib
"""

standard_procedure = False

srcdir = "boost_1_59_0"
def prepare():
	export("HOME", build_dir)
	sed("-e '1 i#ifndef Q_MOC_RUN' \
    -e '$ a#endif'            \
    -i boost/type_traits/detail/has_binary_operator.hpp")
    
def configure():
	export("HOME", build_dir)
	system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python2.7 --prefix=%s/usr" % install_dir)
	system("./b2 \
            variant=release \
            debug-symbols=off \
            threading=multi \
            runtime-link=shared \
            link=shared,static \
            toolset=gcc \
            python=2.7 \
            cflags=-fno-strict-aliasing \
           --layout=system")


def install():
    makedirs(install_dir+"/usr")
    export("HOME", build_dir)
    system("./b2 install threading=multi link=shared --prefix=%s" % install_dir+"/usr")
   # system("./bjam install --prefix=%s" % install_dir+"/usr")
