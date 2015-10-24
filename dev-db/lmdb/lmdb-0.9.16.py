metadata = """
summary @ Symas Lightning Memory-Mapped Database
homepage @ http://symas.com/mdb
license @ OpenLDAP
src_url @ https://github.com/LMDB/$name/archive/LMDB_$version.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-libs/libxslt
"""
srcdir ="lmdb-LMDB_0.9.16/libraries/liblmdb"
standard_procedure = False

def build():
    makedirs("%s/usr/lib"% install_dir)
    makedirs("%s/usr/bin"% install_dir)
    makedirs("%s/usr/man/man1"% install_dir)
    makedirs("%s/usr/share"% install_dir)
    makedirs("%s/usr/include"% install_dir)

    make("prefix=/usr")
 
 
    
def install():
    raw_install("DESTDIR=%s prefix=/usr" % install_dir)

	
