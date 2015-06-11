metadata = """
summary @ Lightweight Display Manager (part of LXDE)
homepage @ http://sourceforge.net/projects/lxdm/
license @ GPL
src_url @ http://downloads.sourceforge.net/lxdm/$name-$version.tar.xz
arch @ ~x86_64
options @ nls debug gtk3
"""

depends = """
common @ sys-libs/pam sys-auth/consolekit x11-libs/libxcb
build @ dev-util/pkg-config >=dev-util/intltool-0.40
"""

opt_runtime = """
nls @ sys-devel/gettext
gtk3 @ x11-libs/gtk+:3
"""



