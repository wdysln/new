metadata = """
summary @ A cross-platform application and UI framework
homepage @ http://qt.nokia.com/ 
license @ GPL3 + LGPL
src_url @ http://download.qt.io/archive/qt/5.5/5.5.0/single/qt-everywhere-opensource-src-5.5.0.tar.xz
arch @ ~x86_64
slot @ 5
"""

depends = """
build @ media-libs/libwebp dev-lang/ruby[yaml]
runtime @ sys-libs/glibc media-libs/tiff media-libs/libpng media-libs/libmng dev-db/sqlite app-misc/ca-certificates sys-libs/glib sys-apps/dbus
	media-libs/fontconfig media-libs/mesa x11-libs/libSM x11-libs/libXrandr x11-libs/libXv x11-libs/libXi media-libs/alsa-lib
	dev-db/unixODBC x11-libs/gtk+:2 media-plugins/gst-plugins-base:0 media-libs/gstreamer:0 dev-util/cmake media-libs/libwebp
"""

srcdir = "qt-everywhere-opensource-src-"+version

def configure():
    system("unset QMAKESPEC")
    export("QT5DIR", build_dir)
    export("PATH", "%s/bin:%s" % (build_dir, get_env("PATH")))
    export("LD_LIBRARY_PATH", "%s/%s" % (build_dir, "lib"))
    
    print system('sed -i "s|-O2|$CXXFLAGS|" mkspecs/common/g++.conf')
    print system('sed -i "/^QMAKE_RPATH/s| -Wl,-rpath,||g" mkspecs/common/g++.conf')
    print system('sed -i "/^QMAKE_LFLAGS\s/s|+=|+= $LDFLAGS|g" mkspecs/common/g++.conf')
    
    raw_configure("-confirm-license -opensource \
            -prefix /usr \
            -docdir /usr/share/doc/qt5 \
            -plugindir /usr/lib/q5t/plugins \
            -importdir /usr/lib/qt5/imports \
            -datadir /usr/share/qt5 \
            -translationdir /usr/share/qt5/translations \
            -sysconfdir /etc \
            -examplesdir /usr/share/doc/qt5/examples \
            -plugin-sql-{sqlite,odbc} \
            -system-sqlite \
            -system-zlib \
            -system-libpng \
            -system-libjpeg \
            -nomake examples \
            -no-rpath \
            -openssl-linked \
            -silent \
            -optimized-qmake \
            -dbus \
            -reduce-relocations \
            -no-separate-debug-info \
            -opengl \
            -no-openvg \
            -glib \
            -skip qtwebengine \
            -gtkstyle")

def build():
    system("unset QMAKESPEC")
    export("QT5DIR", build_dir)
    export("PATH", "%s/bin:%s" % (build_dir, get_env("PATH")))
    export("LD_LIBRARY_PATH", "%s/%s" % (build_dir, "lib"))
    make()

def install():
    raw_install("INSTALL_ROOT=%s" % install_dir)

    #sed("%s%s/pkgconfig/*.pc" % (install_dir, "/usr/lib"), "%s/qt-x11-opensource-src-%s" % (build_dir, version), "/usr")

    #system("find %s/usr/lib -type f -name '*.prl' -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' {} \;" % install_dir)

