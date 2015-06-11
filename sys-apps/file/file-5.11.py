metadata = """
summary @ File type identification utility
homepage @ http://www.darwinsys.com/file/
license @ as-is
src_url @ ftp://ftp.astron.com/pub/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python:2.7
runtime @ sys-libs/glibc sys-libs/zlib
"""

get("python_utils")

standard_procedure = False

configure = lambda: conf()
build = lambda: make()

def install():
    installd()
    insdoc("README", "ChangeLog", "MAINT")
    # install magic library because of lpms uses that library for 
    # identification of file types
    cd("python")
    system("python2 setup.py install --root=%s" % install_dir)

