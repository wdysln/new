metadata = """
summary @ Off-the-Record Messaging Library and Toolkit
homepage @ http://www.cypherpunks.ca/otr/
license @ GPL + LGPL
src_url @ http://www.cypherpunks.ca/otr/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libgcrypt
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

