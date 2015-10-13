metadata = """
summary @ International Components for Unicode library
homepage @ http://www.icu-project.org
license @ icu
src_url @ http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz
arch @ ~x86_64
options @ debug examples static-libs
"""

srcdir = "icu"

depends = """
runtime @ sys-devel/gcc
"""

    
def configure():
    cd("source")
    conf(
        config_enable("debug"),
        config_enable("examples", "samples"),
        config_enable("static-libs", "static"))

def build():
    cd("source")
    make()

def install():
    cd("source")
    raw_install("-j1 DESTDIR=%s" % install_dir)
