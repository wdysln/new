metadata = """
summary @ XML stylesheets for Docbook-xml transformations.
homepage @ http://docbook.sourceforge.net/
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/docbook/docbook-xsl-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libxml2 dev-libs/libxslt 
"""

srcdir = "docbook-xsl-"+version

standard_procedure = False

def prepare():
    patch(level=1)
    copy("%s/Makefile" % filesdir, "Makefile")	
	
def install():
    raw_install("DESTDIR=%s/usr/share/xml/docbook/xsl-stylesheets" % install_dir)
    insinto("VERSION.xsl","/usr/share/xml/docbook/xsl-stylesheets")



