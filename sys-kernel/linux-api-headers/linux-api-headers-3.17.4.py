metadata = """
summary @ Kernel headers sanitized for use in userspace.
homepage @ http://www.kernel.org
license @ GPL-2
src_url @ ftp://ftp.kernel.org/pub/linux/kernel/v3.x/linux-3.17.4.tar.xz
arch @ ~x86_64
"""

standard_procedure = False

srcdir = "linux-3.17.4"

def build():
    make("mrproper")
    make("headers_check")

def install():
    make("INSTALL_HDR_PATH=%s/usr headers_install" % install_dir)
