metadata = """
summary @ LibreOffice Office Suite
homepage @ http://www.libreoffice.org/
license @ GPL-2
src_url @ http://download.documentfoundation.org/libreoffice/src/5.0.1/libreoffice-$version.tar.xz
	  http://download.documentfoundation.org/libreoffice/src/5.0.1/libreoffice-dictionaries-$version.tar.xz
	  http://download.documentfoundation.org/libreoffice/src/5.0.1/libreoffice-help-$version.tar.xz
	  http://download.documentfoundation.org/libreoffice/src/5.0.1/libreoffice-translations-$version.tar.xz
arch @ ~x86_64
"""

depends = """
common @ dev-libs/popt >=x11-libs/gtk+-2.10:2 dev-perl/archive-zip dev-lang/python[threads] app-text/poppler
         media-libs/silgraphite dev-cpp/clucene-core media-libs/glew
"""


get("gnome2_utils", "fdo_mime")

standard_procedure = False


def configure():
    export("LO_PREFIX", "/usr")
    system("/bin/chmod u+x %s/bin/unpack-sources" % build_dir)
    makedirs("%s/external/tarballs"% build_dir)

    system('sed -e "/distro-install-file-lists/d" -i Makefile.in')
    system('sed -e "/ustrbuf/a #include <algorithm>" \
                              -i svl/source/misc/gridprinter.cxx')
    system("/bin/chmod u+x %s/bin/unpack-sources" % build_dir)
    for f in [ "dictionaries", "help", "translations"]:
        name = "libreoffice-%s-%s.tar.xz" % (f, version)
        makesym("%s/%s" % (src_cache,name), "%s/external/tarballs/%s" % (build_dir, name))
        
    append_cxxflags("-I%s/include" % build_dir)

    options =         '--prefix=/usr                   \
                        --sysconfdir=/etc               \
                        --with-vendor=PisiLinux         \
                        --with-lang="tr"               \
                        --with-help                     \
                        --with-myspell-dicts            \
                        --with-alloc=system             \
                        --without-java                  \
                        --without-system-dicts          \
                        --disable-gconf                 \
                        --disable-postgresql-sdbc       \
                        --enable-release-build=yes      \
                        --enable-python=system          \
                        --with-system-boost             \
                        --with-system-curl              \
                        --with-system-cairo             \
                        --with-system-expat             \
                        --with-system-harfbuzz          \
                        --with-system-icu               \
                        --with-system-jpeg              \
                        --with-system-lcms2             \
                        --with-system-libpng            \
                        --with-system-libxml            \
                        --with-system-mesa-headers      \
                        --with-system-nss               \
                        --with-system-openssl           \
                        --with-system-poppler           \
                        --with-system-zlib              \
                        --disable-odk
                        --with-parallelism=%s' % (get_env("JOBS").replace("-j","")))

    system("./autogen.sh %s" % options)
    
def build():
    export("LO_PREFIX", "/usr")
    make("build-nocheck")

def install():
    raw_install("distro-pack-install DESTDIR=%s" % install_dir)


