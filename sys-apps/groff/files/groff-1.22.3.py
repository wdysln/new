metadata = """
summary @ GNU troff text-formatting system
homepage @ http://www.gnu.org/software/groff/groff.html
license @ GPL
src_url @ ftp://ftp.gnu.org/gnu/groff/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-apps/texinfo
"""


def install():
    makedirs("/usr")
    raw_install("DESTDIR=%s" % install_dir)

    makesym("eqn", "/usr/bin/geqn")
    makesym("tbl", "/usr/bin/gtbl")
    makesym("soelim", "/usr/bin/zsoelim")

    insdoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
