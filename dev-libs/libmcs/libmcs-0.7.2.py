metadata = """
summary @ Library which abstracts the storage of configuration settings
homepage @ http://www.atheme.org/project/mcs
license @ BSD
src_url @ https://github.com/atheme/libmcs/archive/libmcs-0.7.2.tar.gz
arch @ ~x86_64
options @ gnome
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libmowgli
build @ dev-util/pkg-config
"""

opt_runtime = """
gnome @ gnome-base/gconf
"""
srcdir = "libmcs-libmcs-0.7.2"
def configure():
    system("./autogen.sh")
    conf(
    "--disable-kconfig",
    config_enable("gnome", "gconf"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "README", "TODO")
