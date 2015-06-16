metadata = """
summary @ C library for encoding, decoding and manipulating JSON data
homepage @ http://www.digip.org/jansson/
license @ MIT
src_url @ http://www.digip.org/$name/releases/$fullname.tar.bz2
arch @ ~x86_64
"""


def configure():
    conf("--disable-gcov", config_enable("introspection"))

