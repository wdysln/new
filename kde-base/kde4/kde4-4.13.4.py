metadata = """
summary @ Meta package for KDE4 desktop
homepage @ http://www.kde.org/
license @ GPL-2
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake
runtime @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4
x11-base/xorg-server >=kde-base/ark-4.14.3 >=kde-base/kde-baseapps-4.14.3 >=kde-base/kate-4.14.3
>=kde-base/kdepimlibs-4.14.3 >=kde-base/kdepim-runtime-4.14.3 >=kde-base/oxygen-icons-4.14.3
>=kde-base/konsole-4.14.3 >=kde-base/kmix-4.14.3 net-p2p/ktorrent >=kde-base/gwenview-4.14.3
>=kde-base/ksnapshot-4.14.3 >=kde-base/kde-l10n-tr-4.14.3 kde-base/networkmanagement
"""

standard_procedure = False

