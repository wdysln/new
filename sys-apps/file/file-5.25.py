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

def configure():
	conf("--datadir=/usr/share/misc \
	--disable-static \
	--enable-fsect-man5")
	
def build():
	make()
	
def install():
	installd()
	
	cd("python")
	export("PYTHONDONTWRITEBYTECODE", "1")
	system("python setup.py install --root=%s" % install_dir)

