metadata = """
summary @ Performance and usability-oriented extensions to C
homepage @ http://www.atheme.org/project/mowgli
license @ BSD-2
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/libmowgli/libmowgli-0.9.50.tar.bz2/104cafd29fe874377169cb7e81c7b50f/libmowgli-0.9.50.tar.bz2
arch @ ~x86_64
options @ examples
"""

def configure():
    conf(
    config_enable("examples"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "README")
