metadata = """
summary @ Library that provides a high-level interface to RDF data MySQL storage support for Redland PostgreSQL storage support for Redland Virtuoso storage support for Redland SQLite storage support for Redland
homepage @ http://librdf.org/
license @ GPL
src_url @ http://download.librdf.org/source/$fullname.tar.gz
arch @ ~x86_64
options @ sqlite virtuoso berkdb xml static-libs ssl threads
"""

depends = """
runtime @ dev-libs/rasqal media-libs/raptor:2.0
"""

opt_runtime = """
sqlite @ dev-db/sqlite
virtuoso @ dev-db/unixODBC dev-db/virtuoso
berkdb @ sys-libs/db
xml @ dev-libs/libxml2 || dev-libs/expat
ssl @ dev-libs/openssl
"""

def configure():
	patch()

def configure():
    if opt("xml"):
        parser = "libxml"
    else:
        parser = "expat"

    conf(
    config_with("berkdb", "bdb"),
    config_with("sqlite"),
    "--enable-release",
    "--with-xml-parser=%s" % parser,
	config_enable("static-libs", "static"),
	config_with("ssl", "openssl-digests"),
	config_with("threads"))

def install():
	raw_install("DESTDIR=%s" % install_dir)
	system("rm -fr %s/usr/lib/redland" % install_dir)

	if opt("sqlite"):
		system("install -dm755 %s/usr/lib/redland" % install_dir)
		system("install -m755 src/.libs/librdf_storage_sqlite.so %s/usr/lib/redland/" % install_dir)

	if opt("virtuoso"):
		system("install -dm755 %s/usr/lib/redland" % install_dir)
		system("install -m755 src/.libs/librdf_storage_virtuoso.so %s/usr/lib/redland/" % install_dir)

