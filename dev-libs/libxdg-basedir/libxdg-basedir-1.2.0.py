metadata = """
summary @ An implementation of the XDG Base Directory specifications.
homepage @ http://n.ethz.ch/student/nevillm/download/libxdg-basedir
license @ MIT
src_url @ https://github.com/devnev/$name/archive/$fullname.tar.gz
arch @ ~x86_64
options @ static-libs
"""

def configure():
    conf(
    "--disable-dependency-tracking ",
    config_enable("static-libs", "static"))


