metadata = """
summary @ A collection of color schemes from vim.org
homepage @ http://www.vim.org/
license @ GPL-2
src_url @ http://hadronproject.org/distfiles/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ app-editors/vim
"""

standard_procedure = False

def prepare():
    patch()

def install():
    cd("colors")
    insinto("*.vim", "/usr/share/vim/vimfiles/colors")
