metadata = """
summary @ Hebrew spell-checker
homepage @ http://www.ivrix.org.il/projects/spell-checker/
license @ GPL
src_url @ http://hspell.ivrix.org.il/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib dev-lang/perl 
build @ app-text/hunspell sys-apps/gawk
"""

def prepare():
    patch(level=1)

def configure():
    conf("--enable-linginfo", 
            "--enable-fatverb")

def build():
    make(j=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)

"""
FIXME
  install -dm755 ${pkgdir}/usr/share/myspell/dicts
  pushd $pkgdir/usr/share/myspell/dicts
    for file in $pkgdir/usr/share/hunspell/*; do
      ln -sv /usr/share/hunspell/$(basename $file) .
    done
  popd
"""
