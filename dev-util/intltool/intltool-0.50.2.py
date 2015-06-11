metadata = """
summary @ The internationalization tool collection
homepage @ https://edge.launchpad.net/intltool
license @ GPL
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/intltool/intltool-0.50.2.tar.gz/23fbd879118253cb99aeac067da5f591/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-perl/XML-Parser
"""

def configure():
    system('perl -e "require XML::Parser"')
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)
