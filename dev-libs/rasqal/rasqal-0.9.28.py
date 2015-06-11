metadata = """
summary @ A free C library that handles Resource Description Framework (RDF) query syntaxes, query construction and query execution returning result bindings
homepage @ http://librdf.org/rasqal
license @ GPL + LGPL
src_url @ http://download.librdf.org/source/$fullname.tar.gz
arch @ ~x86_64
options @ pcre crypt xml gmp static-libs
"""

depends = """
runtime @ media-libs/raptor:2.0
"""

opt_runtime = """
gmp @ dev-libs/gmp || dev-libs/mpfr
xml @ dev-libs/libxml2
crypt @ dev-libs/libgcrypt
pcre @ dev-libs/pcre
"""

def configure():
    if opt("pcre"):
        regex = "pcre"
    else:
        regex = "posix"

    if opt("gmp"):
        decimal = "gmp"
    else:
        decimal = "mpfr"

    if opt("crypt"):
        digest = "gcrypt"
    else:
        digest = "internal"

	conf(
	config_enable("pcre"),
	config_enable("static-libs", "static"),
	config_enable("xml", "xml2"),
	"--with-regex-library=%s" % regex,
	"--with-digest-library=%s" % digest,
	"--with-decimal=%s" % decimal,
	"--enable-release")

def install():
	raw_install("DESTDIR=%s" % install_dir)


