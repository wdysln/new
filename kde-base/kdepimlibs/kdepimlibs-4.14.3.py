metadata = """
summary @ KDE PIM Libraries
homepage @ https://projects.kde.org/projects/kde/kdepimlibs
license @ GPL-2 LGPL FDL
src_url @ http://download.kde.org/stable/$version/src/$name-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde-base/kdelibs kde-base/akonadi dev-util/cmake dev-util/automoc4 x11-libs/libX11 x11-libs/libXext dev-libs/qjson dev-libs/libical 
dev-libs/cyrus-sasl app-crypt/gpgme dev-libs/libxslt dev-libs/qjson app-crypt/gpgme
"""
#net-dns/openldap
get("main/kde4_utils")


    
