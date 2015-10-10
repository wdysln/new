metadata = """
summary @ A jukebox, tagger and music collection manager
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/krdc/krdc-4.14.3.tar.xz/7e796905eb8579e457c6ead2f1c21525/krdc-4.14.3.tar.xz
arch @ ~x86_64
"""

depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 
        >=kde-base/kde-workspace-4.11.4 net-libs/libvncserver
"""

get("main/kde4_utils")

