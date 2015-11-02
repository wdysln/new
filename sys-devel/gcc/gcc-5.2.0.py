metadata = """
summary @ The GNU Compiler Collection
homepage @ http://gcc.gnu.org/
license @ GPL-3 LGPL-3
src_url @ ftp://gcc.gnu.org/pub/gcc/releases/$fullname/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ sys-devel/binutils dev-libs/mpc >=sys-libs/zlib-1.1.4 >=dev-libs/mpfr-2.4.2
#build @ >=sys-apps/texinfo-4.8 >=sys-devel/bison-1.875 >=sys-devel/flex-2.5.4
"""

cflags = "-O2 -g"

def prepare():
    export("CFLAGS", cflags)
    export("CXXFLAGS", cflags)
    # shelltools.export("LDFLAGS", "")

    export("CC", "gcc")
    export("CXX", "g++")
    export("LC_ALL", "en_US.UTF-8")
  
def configure():
    sed("-i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in")
    sed("-i -e /autogen/d -e /check.sh/d fixincludes/Makefile.in")
    # Hadron installs x86_64 libraries /lib
    sed("-i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64")

    makedirs("../gcc-build"); cd("../gcc-build")

    conf("--enable-shared",
            "--enable-threads=posix",
            "--with-system-zlib",
            "--enable-__cxa_atexit",
            "--enable-languages=c,c++,lto",
            "--disable-libunwind-exceptions",
            "--enable-clocale=gnu",
            "--disable-libstdcxx-pch",
            "--enable-libstdcxx-time",
            "--enable-gnu-unique-object",
            "--enable-linker-build-id",
            "--enable-lto",
            "--enable-gold",
            "--enable-ld=default",
            "--enable-plugin",
            "--with-linker-hash-style=gnu",
            "--enable-multilib",
            "--with-arch_32=i686",
            "--disable-libssp",
            "--build=x86_64-pc-linux-gnu",
            "--disable-build-with-cxx",
            "--disable-build-poststage1-with-cxx",
            "--enable-checking=release",
            "--with-pkgversion='Hadron GNU/Linux'",
            run_dir=build_dir)

def build():
    cd("../gcc-build")
   # make()
    make('BOOT_CFLAGS="%s" profiledbootstrap' % cflags)

def install():
    cd("../gcc-build")
    # install gcc
    raw_install("DESTDIR=%s" % install_dir)
    # create symlinks
    makesym("/usr/bin/gcc" , "/usr/bin/cc")
    makesym("/usr/bin/cpp" , "/lib/cpp")
