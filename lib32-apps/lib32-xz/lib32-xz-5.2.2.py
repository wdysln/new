metadata = """
summary @ Library and command line tools for XZ and LZMA compressed files
homepage @ http://tukaani.org/xz/
license @ GPL LGPL custom
src_url @ http://tukaani.org/xz/xz-$version.tar.gz
arch @ ~x86_64
"""
srcdir ="xz-%s" %version

get("main/lib32_utils")