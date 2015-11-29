metadata = """
summary @ DOS filesystem utilities
homepage @ https://github.com/dosfstools/dosfstools
license @ GPL2
src_url @ https://github.com/dosfstools/dosfstools/releases/download/v$version/$fullname.tar.xz
arch @ ~x86_64
"""


def build():
    make

def install():
    raw_install("DESTDIR=%s PREFIX=/usr" % install_dir)


