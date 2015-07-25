metadata = """
summary @ RAR decompressor
homepage @ http://www.info-zip.org/pub/infozip/Zip.html
license @ unRAR
src_url @ http://www.rarlab.com/rar/unrarsrc-5.2.4.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

srcdir = "unrar"

def build():
    make()

def install():
    
    insexe("unrar", "/usr/bin/")

    insdoc("readme.txt","license.txt")
