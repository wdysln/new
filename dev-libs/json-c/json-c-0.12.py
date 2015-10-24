metadata = """
summary @ A JSON implementation in C
homepage @ https://github.com/json-c/json-c/wiki
license @ MIT
src_url @ https://s3.amazonaws.com/json-c_releases/releases/json-c-0.12.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
def prepare():
    sed("-i s/-Werror// Makefile.in")  
    
def configure():
    conf("--disable-static")

def build():
    make()
    make("check")
    
def install():
	installd()    

