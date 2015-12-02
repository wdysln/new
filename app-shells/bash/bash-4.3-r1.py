metadata = """
summary @ The standard GNU Bourne again shell
homepage @ http://tiswww.case.edu/php/chet/bash/bashtop.html
license @ GPL-3
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ net nls afs mem-scramble plugins
arch @ ~x86_64
"""

depends = """
common @ sys-libs/ncurses
build @ sys-libs/readline
"""
cfgsettings = """-DDEFAULT_PATH_VALUE=\'\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\' \
                 -DSTANDARD_UTILS_PATH=\'\"/bin:/usr/bin:/sbin:/usr/sbin\"\' \
                 -DSYS_BASHRC=\'\"/etc/bash/bashrc\"\' \
                 -DSSH_SOURCE_BASHRC"""
                 
                 
def prepare():
    for i in xrange(1, 42):
        fetch("http://ftp.gnu.org/gnu/bash/bash-4.3-patches/bash43-%03d" % i, location=build_dir)

    for f in xrange(1, 42):
        patch("bash43-%03d" % f, location=build_dir)

def configure():
    export("CFLAGS", "-D_GNU_SOURCE -DRECYCLES_PIDS %s" % cfgsettings)
    autoconf()
    myconf = ""
    if not opt("nls"):
        myconf += " --disable-nls"

    conf(config_with("afs"),
        config_enable("mem-scramble"),
        config_with("mem-scramble", "bash-malloc"),
        config_enable("net", "net-redirections"),
        "--with-curses",
        "--enable-readline",
        "--disable-profiling",
        "--with-installed-readline",
        myconf)


def install():
    if opt("plugins"):
        make("-C examples/loadables all others")

    raw_install("DESTDIR=%s install" % install_dir)

    makedirs("/bin")
    move("%s/usr/bin/bash" % install_dir, "/bin/bash")
    makesym("/bin/bash", "/bin/sh")

    makedirs("/etc/skel")
    insexe(joinpath(filesdir, "bashrc"), "/etc/bash/bashrc")
   # insfile(joinpath(filesdir, "dot-bashrc"), "/etc/skel/.bashrc")
   # insfile(joinpath(filesdir, "dot-bash_profile"), "/etc/skel/.bash_profile")
    #insfile(joinpath(filesdir, "dot-bash_logout"), "/etc/skel/.bash_logout")
    insexe(joinpath(filesdir, "dircolors"), "/etc/DIR_COLORS")

    insdoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
