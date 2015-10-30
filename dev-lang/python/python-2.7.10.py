metadata = """
summary @ A high-level scripting language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/$version/Python-$version.tar.xz
options @ ipv6 examples
arch @ ~x86_64
slot @ 2.7
"""
srcdir = "Python-2.7.10"


depends = """
common @ dev-db/sqlite app-arch/bzip2 >=sys-libs/zlib-1.1.3 
dev-libs/libffi dev-util/intltool sys-libs/gdbm
"""


def prepare():
    sed('-i "/progname =/s/python/python2.7/" Python/pythonrun.c')
    patch(level=1)
    for i in ('expat', 'zlib', '_ctypes/darwin'): #'_ctypes/libffi'):
        rmdir('Modules/%s' % i)
    copytree("Lib/plat-linux2", "%s/Lib/plat-linux3" % build_dir)
    rmfile("Lib/distutils/command/*.exe")
    append_cflags("-fwrapv")

def configure():
    raw_configure("--prefix=/usr",
            "--with-fpectl",
            "--infodir=/usr/share/info",
            "--mandir=/usr/share/man",
            "--with-libc=''",
            config_enable("ipv6"),
            "--with-threads",
            "--enable-unicode=ucs4",
            "--with-dbmliborder=gdbm",
            "--enable-shared",
            "--with-system-expat",
            "--with-system-ffi")

def build():
    #export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s altinstall maninstall" % install_dir)

    libdir = "/usr/lib/python%s" % slot
 
    # the spec no support tk
    rmfile("/usr/bin/idle")
    for item in ('idlelib', 'lib-tk'):
        rmdir(joinpath(libdir, item))


    if opt("examples"):
        makedirs("/usr/share/doc/%s" % fullname)
        copy("Tools", "/usr/share/doc/%s" % fullname)

    insdoc("LICENSE", "README")
    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
