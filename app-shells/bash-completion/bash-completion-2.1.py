metadata = """
summary @ Programmable completion for bash
homepage @ http://bash-completion.alioth.debian.org
license @ GPL-3
src_url @ http://bash-completion.alioth.debian.org/files/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ app-shells/bash
build @ sys-libs/readline
"""

def build():
    make("bash_completion.sh")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    blacklist = ["cal", "chsh", "dmesg", "eject", "hd", "hexdump", "hwclock", "ionice", "look", "ncal", "nmcli", "newgrp", "makepkg", "renice", "rtcwake", "su"]
    for comp in blacklist:
       system("rm -rf usr/share/bash-completion/completions/%s" % comp)    
       
       