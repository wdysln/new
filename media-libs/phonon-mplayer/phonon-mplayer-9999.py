metadata = """
summary @ Mplayer Backend for Phonon
homepage @ https://projects.kde.org/projects/kdesupport/phonon/phonon-mplayer/repository
license @ GPL
arch @ ~x86_64
"""

depends = """
common @ media-libs/phonon media-video/mplayer
build @ dev-lang/python:2.7 dev-vcs/git
"""

standard_procedure = False

def prepare():
    notify("cloning git://anongit.kde.org/phonon-mplayer")
    if not system("git clone git://anongit.kde.org/phonon-mplayer"):
        error("git clone failed.")

def build():
    cd("phonon-mplayer/build")
    system("cmake ../ \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON")
    make()

def install():
    cd("phonon-mplayer/build")
    installd()
