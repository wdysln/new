metadata = """
summary @ Exif and Iptc metadata manipulation library and tools
homepage @ http://exiv2.org/
license @ GPL2
src_url @ http://www.exiv2.org/$fullname.tar.gz
arch @ ~x86_64
options @ nls xmp zlib
"""

depends = """
runtime @ sys-devel/gcc sys-devel/gettext sys-libs/zlib
"""

get("main/cmake_utils")


