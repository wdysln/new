metadata = """
summary @ Boost Libraries for C++
homepage @ http://www.boost.org/
license @ Boost-1.0
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name_1_55_0.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-libs/icu dev-lang/python:2.7 app-arch/bzip2 sys-libs/zlib
"""

standard_procedure = False

srcdir = "boost_1_55_0"

def configure():
    system("./bootstrap.sh")

def install():
    makedirs(install_dir+"/usr")
    system("./bjam install --prefix=%s" % install_dir+"/usr")
