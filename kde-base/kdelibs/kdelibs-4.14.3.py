metadata = """
summary @ KDE Core Libraries
homepage @ http://www.kde.org/
license @ GPL + LGPL + FDL
src_url @ http://download.kde.org/stable/4.14.3/src/kdelibs-4.14.3.tar.xz
arch @ ~x86_64
options @ soprano
"""

depends = """
runtime @ app-misc/strigi kde-base/attica x11-misc/libxss app-arch/xz dev-libs/openssl 
	app-crypt/qca dev-libs/libdbusmenu-qt sys-auth/polkit-qt dev-libs/grantlee 
	x11-misc/shared-mime-info app-text/enchant media-libs/giflib media-libs/jasper media-libs/openexr 
	media-libs/ilmbase x11-misc/xdg-utils media-libs/phonon x11-themes/hicolor-icon-theme sys-power/upower 
	sys-fs/udisks:2 x11-libs/libXcursor app-text/docbook-xsl-stylesheets app-text/docbook-xml-dtd:4.2
build @ dev-util/pkg-config dev-util/cmake dev-util/automoc4 dev-util/intltool app-text/hspell media-libs/mesa
"""

#opt_runtime = """
#soprano @ dev-libs/soprano dev-libs/shared-desktop-ontologies
#"""

get("main/fdo_mime", "main/cmake_utils", "main/extract_utils")

extract = lambda: tar_extract("%s.tar.xz" % fullname)
build = lambda: (cd("build"), make())
prepare = lambda: makedirs("build")
install = lambda: cmake_utils_install(builddir="build")

def configure():
    cd("build")
    cmake_conf("-DCMAKE_SKIP_RPATH=ON",
            "-DKDE_DISTRIBUTION_TEXT='Hadron GNU/Linux'",
            "-DAutomoc4_DIR=/usr/lib/automoc4",
            "-DWITH_Soprano=OFF",
            "-DKDE4_BUILD_TESTS=OFF",
            "-DCMAKE_SKIP_RPATH=ON",
            "-DWITH_FAM=OFF",
            "-DWITH_HUpnp=OFF",
            "-DDOCBOOKXSL_DIR=/usr/share/xml/docbook/docbook-xsl-1.76.1", sourcedir=build_dir)

def post_install():
    xdg_icon_resource()
    update_mime_database()
