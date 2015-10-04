metadata = """
summary @ Implementation for atomic memory update operations
homepage @ http://www.hpl.hp.com/research/linux/atomic_ops/
license @ MIT boehm-gc GPL-2+
src_url @ https://github.com/ivmai/$name/archive/$name-7_4_2.tar.gz
arch @ ~x86_64
"""

srcdir = "%s-libatomic_ops-7_4_2" % name

install = lambda: installd()
