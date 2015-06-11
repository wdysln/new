metadata = """
summary @ POSIX compliant regexp matching library. Includes agrep for aproximate grepping
homepage @ http://laurikari.net/tre/index.html
license @ custom + BSD
src_url @ http://laurikari.net/tre/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
	conf(
	"--enable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
#hatali degil aslinda, sikik doclar karisti ne nereye konacak amk http://projects.archlinux.org/svntogit/community.git/tree/tre/trunk/PKGBUILD
