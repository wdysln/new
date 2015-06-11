metadata = """
summary @ Pico editor clone with enhancements
homepage @ http://www.nano-editor.org
license @ GPL-2
src_url @ http://www.nano-editor.org/dist/v2.4/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/ncurses
"""

def configure():
    conf("--enable-color",
        "--enable-nanorc",
        "--enable-multibuffer",
        "--disable-speller",
        "--disable-wrapping-as-root")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makesym("/usr/bin/nano", "/bin/nano")
    insdoc("ChangeLog*", "README", "doc/nanorc.sample", "AUTHORS",
            "BUGS", "NEWS", "TODO", "COPYING*", "THANKS", "UPGRADE")
