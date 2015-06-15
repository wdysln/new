metadata ="""
summary @ ENCA detects the character coding of a file and converts it if desired
homepage @ http://gitorious.org/enca
license @ GPL-2
src_url @ http://dl.cihar.com/$name/$name-$version.tar.xz
options @ doc recode
arch @ ~x86_64
"""

opt_build = """
recode @ app-text/recode
"""

opt_runtime = """
recode @ app-text/recode
"""

def configure():
    raw_configure("--prefix=/usr",
            "--enable-external",
            config_enable("doc", "gtk-doc"),
            config_with("recode", "librecode"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
