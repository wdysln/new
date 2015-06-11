metadata = """
summary @ KDE Core Libraries
homepage @ http://www.kde.org/
license @ GPL + LGPL + FDL
src_url @ http://download.kde.org/stable/4.12.0/src/kdelibs-4.12.0.tar.xz
arch @ ~x86_64
options @ semantic ssl sse sse2 3dnow mmx
"""

depends = """
runtime @ app-misc/strigi kde-base/attica x11-misc/libxss app-arch/xz 
	app-crypt/qca dev-libs/libdbusmenu-qt sys-auth/polkit-qt dev-libs/grantlee 
	x11-misc/shared-mime-info app-text/enchant media-libs/giflib media-libs/jasper media-libs/openexr 
	media-libs/ilmbase x11-misc/xdg-utils media-libs/phonon x11-themes/hicolor-icon-theme sys-power/upower 
	sys-fs/udisks x11-libs/libXcursor app-text/docbook-xsl-stylesheets app-text/docbook-xml-dtd:4.2
build @ dev-util/pkg-config dev-util/cmake dev-util/automoc4 dev-util/intltool app-text/hspell media-libs/mesa
"""

opt_runtime = """
semantic @ dev-libs/soprano dev-libs/shared-desktop-ontologies
ssl @ dev-libs/openssl
"""

get("main/fdo_mime", "main/cmake_utils", "main/extract_utils")

extract = lambda: tar_extract("%s.tar.xz" % fullname)
build = lambda: (cd("build"), make(j=1))
install = lambda: cmake_utils_install(builddir="build")

def prepare():
    makedirs("build")
    patch(level=1)

def configure():
    #Library should learn how to rock for this:
    export ("Automoc4_DIR","=/usr/lib/automoc4") 
    export ("CMAKE_PREFIX_PATH","=/usr")
    extraconf = ""
    if opt("semantic"):
        extraconf += " -DWITH_Soprano=ON -DWITH_SharedDesktopOntologies=ON "
    else:
        extraconf += " -DWITH_Soprano=OFF -DWITH_SharedDesktopOntologies=OFF "

    cd("build")
    cmake_conf("-DCMAKE_SKIP_RPATH=ON",
            "-DWITH_HSPELL=OFF",
            "-DWITH_ASPELL=OFF",
            "-DBUILD_libkactivities=OFF",
            "-DKDE_DISTRIBUTION_TEXT='Hadron GNU/Linux'",
            "-DAutomoc4_DIR=/usr/lib/automoc4",
            "-DSTRIGI_INCLUDE_DIR=/usr/include/strigi",
            "-DHTML_INSTALL_DIR=/usr/share/doc/kde/html",
            "-DKDE_DEFAULT_HOME='.kde4'",
            "-DDOCBOOKXSL_DIR=/usr/share/xml/docbook/docbook-xsl-1.76.1",
            cmake_config_with("ssl"),
            cmake_config_have("mmx"),
            cmake_config_have("sse"),
            cmake_config_have("sse2"),
            cmake_config_have("3dnow"), extraconf, sourcedir=build_dir)

def build():
    export("HOME", build_dir)
    cd ("build")
    make()

def post_install():
    xdg_icon_resource()
    update_mime_database()
