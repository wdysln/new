metadata = """
summary @ VLC Backend for Phonon
homepage @ https://projects.kde.org/projects/kdesupport/phonon/phonon-vlc
license @ GPL
arch @ ~x86_64
"""

depends = """
common @ media-libs/phonon media-video/vlc[ogg,vorbis] x11-libs/qt
build @ dev-vcs/git >=dev-util/automoc4-0.9.87 dev-util/pkg-config
"""

standard_procedure = False

def prepare():
    notify("cloning git://anongit.kde.org/phonon-vlc")
    if not system("git clone git://anongit.kde.org/phonon-vlc"):
        error("git clone failed.")

def build():
    cd("phonon-vlc")
    makedirs("build")
    cd("build")
    system("cmake ../ \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON")
    make()

def install():
    cd("phonon-vlc/build")
    installd()

def post_install():
    notify("** To make KDE detect the new backend without reboot, run: ")
    notify("** kbuildsycoca4 --noincremental ")
