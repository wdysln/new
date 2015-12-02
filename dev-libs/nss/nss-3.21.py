metadata = """
summary @ Mozilla Network Security Services
homepage @ http://www.mozilla.org/projects/security/pki/nss/
license @ MPL GPL
src_url @ https://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_21_RTM/src/nss-3.21.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/nspr dev-db/sqlite sys-libs/zlib
build @ dev-lang/perl
"""

def prepare():
    patch("nss-3.21-standalone-1.patch", level=1)

def build():
    cd("nss")
    make("nss_build_all BUILD_OPT=1 NSPR_INCLUDE_DIR=/usr/include/nspr \
            USE_SYSTEM_ZLIB=1 ZLIB_LIBS=-lz USE_64=1 NSS_USE_SYSTEM_SQLITE=1", j=1)

def install():
    for binary in ("certutil", "cmsutil", "crlutil", "modutil", "pk12util", \
            "shlibsign", "signtool", "signver", "ssltap", "nss-config"):
        insinto("dist/Linux*/bin/%s" % binary, "/usr/bin", sym=False)

    for lib in ["*.chk","*.so","libcrmf.a"]:
        insinto("dist/Linux*/lib/%s" % lib, "/usr/lib", sym=False)

   # insinto("mozilla/dist/*.OBJ/lib/libcrmf.a", "/usr/lib/", sym=False)

    # Headers
    for header in ["dist/private/nss/*.h", "dist/public/nss/*.h"]:
        insinto(header, "/usr/include/nss", sym=False)

    # Drop executable bits from headers
    setmod("0644", "%s/usr/include/nss/*.h" % install_dir)

    insfile("dist/Linux*/lib/pkgconfig/nss.pc", "/usr/lib/pkgconfig/nss.pc")

  #  for lib in ('libssl3.so', 'libsmime3.so', 'libnssutil3.so', 'libnss3.so', 
   #         'libsoftokn3.so', 'libfreebl3.so', 'libnssckbi.so', 'libnssdbm3.so'):
    #    inslib("mozilla/dist/*.OBJ/lib/%s" % lib, "/usr/lib/%s" % lib)
