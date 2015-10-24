metadata = """
summary @ Desktop-independent graphical login manager for X11
homepage @ http://slim.berlios.de/
license @ GPL2
src_url @ https://github.com/sddm/sddm/releases/download/v0.12.0/sddm-0.12.0.tar.xz
arch @ ~x86_64
options @ pam
"""

#FIXME: SLIM gives 'Failed to execute login command' error

depends = """
runtime @ x11-libs/libXmu x11-libs/libX11 x11-libs/libXpm x11-libs/libXft
media-libs/libpng media-libs/jpeg
build @ dev-util/pkg-config x11-proto/xproto
"""

opt_runtime = """
pam @ sys-libs/pam
"""

get("cmake_utils")

#To fix a compilation error related with libXmu


def configure():
    cmake_conf("-DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=Release  \     \
      -Wno-dev ")
        
def install():
    raw_install("DESTDIR=%s" % install_dir)
