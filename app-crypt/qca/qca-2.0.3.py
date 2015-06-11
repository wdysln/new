metadata = """
summary @ Qt Cryptographic Architecture
homepage @ http://delta.affinix.com/qca/
license @ LGPL
src_url @ http://delta.affinix.com/download/qca/2.0/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt app-misc/ca-certificates
"""

def configure():
    patch("qca2-sha2-digest-support-kde-svn-992617.diff", level=3)
    patch("qca-2.0.3+gcc-4.7.patch", level=0)    
      
            
    raw_configure("--prefix=/usr",
            "--disable-tests",
            "--certstore-path=/etc/ssl/certs/ca-certificates.crt",
            "--release",
            "--no-separate-debug-info")

def install():
    raw_install("INSTALL_ROOT=%s" % install_dir)
    insdoc("COPYING")

