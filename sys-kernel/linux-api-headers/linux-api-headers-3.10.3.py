metadata = """
summary @ Kernel headers sanitized for use in userspace.
homepage @ http://www.kernel.org
license @ GPL-2
src_url @ http://ftp.isu.edu.tw/pub/Linux/kernel/v3.x/linux-$version.tar.xz
arch @ ~x86_64
"""

standard_procedure = False

srcdir = "linux-3.10.3"

def build():
    make("mrproper")
    make("headers_check")

def install():
    make("INSTALL_HDR_PATH=%s/usr headers_install" % install_dir)
