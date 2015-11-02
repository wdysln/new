metadata = """
summary @ base system
homepage @ http://hadronproject.org/
license @ GPL-3
arch @ ~x86_64
slot @ 2
"""

depends = """
runtime @ sys-apps/lpms sys-devel/make sys-devel/automake sys-devel/autoconf app-editors/nano app-arch/tar 
app-arch/bzip2 app-arch/gzip sys-apps/grep sys-apps/gawk sys-apps/diffutils sys-apps/baselayout 
net-misc/wget app-arch/xz sys-process/procps sys-apps/less dev-vcs/git sys-devel/libtool sys-apps/kbd
net-misc/dhcpcd sys-libs/zlib sys-apps/util-linux sys-apps/texinfo dev-util/pkg-config sys-devel/patch 
sys-process/lsof sys-apps/dbus sys-apps/systemd sys-devel/bison app-admin/syslog-ng sys-fs/sysfsutils sys-apps/net-tools
net-misc/iputils sys-apps/iproute2 sys-apps/inetutils dev-libs/isl dev-libs/libsigsegv dev-libs/libunistring
dev-libs/guile dev-libs/gc
"""

standard_procedure = False

