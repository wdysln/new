metadata = """
summary @ Documentation tool for public library API
homepage @ http://www.gtk.org/gtk-doc/
license @ GPL + FDL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/$version/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ app-text/docbook-xsl-stylesheets
runtime @ dev-lang/perl
build @ dev-util/pkg-config app-text/docbook-xml dev-util/itstool
"""

def configure():
    conf()

def build():
    installd()
