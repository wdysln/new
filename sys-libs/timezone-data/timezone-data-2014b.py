metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzcode2014b.tar.gz
http://www.iana.org/time-zones/repository/releases/tzdata2014b.tar.gz
arch @ ~x86_64
"""

standard_procedure = False
"""
def prepare():
    cd(dirname(build_dir))
    patch()
"""
def build():
    cd(dirname(build_dir))
    make()

def install():
    cd("..")
    raw_install('DESTDIR=%s' % install_dir)
   
