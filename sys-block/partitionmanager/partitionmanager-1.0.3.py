metadata = """
summary @ A A KDE utility that allows you to manage disks, partitions, and file systems
homepage @ https://sourceforge.net/projects/partitionman/
license @ GPL2
src_url @ http://downloads.sourceforge.net/partitionman/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kde-runtime-4.8 dev-libs/libatasmart sys-fs/e2fsprogs
build @ dev-util/cmake sys-block/parted
"""

get("main/kde4_utils", "main/fdo_mime")

def post_install():
    xdg_icon_resource()
