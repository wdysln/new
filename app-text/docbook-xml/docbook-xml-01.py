metadata = """
summary @ A widely used XML scheme for writing documentation and help
homepage @ http://www.oasis-open.org/docbook/
license @ MIT
src_url @ http://www.docbook.org/xml/4.1.2/docbkx412.zip
http://www.oasis-open.org/docbook/xml/4.1/docbkx41.zip
http://www.docbook.org/xml/4.2/docbook-xml-4.2.zip
http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
http://www.docbook.org/xml/4.4/docbook-xml-4.4.zip
http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip
arch @ ~x86_64
slot @ 4.5
"""

depends = """
runtime @ dev-libs/libxml2
build @ app-text/sgml-common
"""

srcdir = ""

standard_procedure = False


def install():
	for vers in ["4.1.2", "4.2", "4.3", "4.4", "4.5"]:
		insinto("*.dtd", "/usr/share/xml/docbook/xml-dtd-%s" % vers)
		insinto("*.mod", "/usr/share/xml/docbook/xml-dtd-%s" % vers)
		insinto("docbook.cat", "/usr/share/xml/docbook/xml-dtd-%s" % vers)
		insinto("ent/*.ent", "/usr/share/xml/docbook/xml-dtd-%s/ent" % vers)
		
	insfile("%s/docbook" % filesdir, "/etc/xml/docbook")
	insfile("%s/catalog" % filesdir, "/etc/xml/catalog")
