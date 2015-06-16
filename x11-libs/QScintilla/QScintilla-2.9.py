metadata = """
summary @ Qt4 port of Scintilla
homepage @ http://www.riverbankcomputing.co.uk/qscintilla
license @ GPL2 + GPL3
src_url @ http://downloads.sourceforge.net/pyqt/$name-gpl-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt
"""
srcdir ="QScintilla-gpl-%s" % $version
standard_procedure = False


def build():
    export("HOME", build_dir)
    cd("Qt4Qt5")
    system("qmake qscintilla.pro")
    make()

def install():
    export("HOME", build_dir)
    cd("Qt4Qt5")
    raw_install("DESTDIR=%s" % install_dir)

   