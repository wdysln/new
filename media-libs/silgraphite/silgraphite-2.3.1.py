metadata = """
summary @  SILGraphite - a "smart font" rendering engine - the libs and headers
homepage @  http://graphite.sil.org/
license @  custom_SIL Dual license
src_url @  http://downloads.sourceforge.net/silgraphite/graphite2-1.2.4.tgz
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc
"""
srcdir ="graphite2-1.2.4"

get("main/cmake_utils")

