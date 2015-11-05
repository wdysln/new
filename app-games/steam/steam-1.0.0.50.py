metadata = """
summary @ Digital distribution client bootstrap package
homepage @ http://steampowered.com/
license @ custom
src_url @ http://repo.steampowered.com/steam/pool/steam/s/steam/steam_1.0.0.50.tar.gz
arch @ ~x86_64
options @ nls static-libs threads
"""

standard_procedure = False

srcdir ="%s" %name

def prepare():
    patch(level=1)


def build():
    make()
    
    
def install():
    raw_install('DESTDIR=%s' % install_dir)
   # insdoc('AUTHORS', 'LICENSE', 'NEWS', 'README', 'THANKS')
