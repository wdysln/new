metadata = """
summary @ Multi-purpose desktop calculator 
homepage @ http://qalculate.sourceforge.net/ 
license @ GPL 
src_url @ http://downloads.sourceforge.net/sourceforge/qalculate/$name-$version.tar.gz 
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/readline dev-cpp/glibmm sys-libs/ncurses dev-libs/libxml2 sci-libs/cln
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

#TODO perlxml istiyor amk
