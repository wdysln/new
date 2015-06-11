metadata = """
summary @ A scalable icon theme called Faenza (KDE Mod)
homepage @ http://kde-look.org/content/show.php?content=143890
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/kfaenza-icon-theme/kfaenza-icon-theme-0.8.9.tar.gz/95e9f287da7a0fd76fb406d313eee77e/kfaenza-icon-theme-0.8.9.tar.gz
license @ GPL
arch @ ~x86_64
"""

standard_procedure = False

get("main/extract_utils")

srcdir = "KFaenza"

def extract():
    if not isfile("KFaenza.tar.bz2"):
        copy("%s/vYjR0NQ" % src_cache, "%s/KFaenza.tar.bz2" % src_cache)
    tar_extract("KFaenza.tar.bz2")

def install():
    cd("..")
    copytree("KFaenza", "/usr/share/icons/KFaenza")

