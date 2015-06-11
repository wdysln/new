metadata = """
summary @ XML stylesheets for Docbook-xml transformations.
homepage @ http://docbook.sourceforge.net/
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/docbook/docbook-xsl-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libxml2 dev-libs/libxslt app-text/docbook-xml-dtd app-text/build-docbook-catalog
"""

srcdir = "docbook-xsl-"+version

standard_procedure = False

def install():
    #pkgroot = "/usr/share/sgml/docbook/xsl-stylesheets"
    pkgroot="usr/share/xml/docbook/docbook-xsl-%s" % version

    makedirs(pkgroot)

    insinto("*", pkgroot)
    insdoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README",
            "RELEASE-NOTES.txt", "TODO", "VERSION")

def post_install():
    system("/usr/bin/build-docbook-catalog")
