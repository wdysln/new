metadata = """
summary @ Portable lossless data compression library
homepage @ http://www.oberhumer.com/opensource/lzo
license @ GPL 
src_url @ http://www.oberhumer.com/opensource/lzo/download/$fullname.tar.gz
arch @ ~x86_64
"""

def configure():
    conf("--enable-shared")

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc('AUTHORS', 'ChangeLog', 'NEWS', 'README', 'THANKS')
