metadata = """
summary @ A scalable icon theme called Faenza
homepage @ http://code.google.com/p/faenza-icon-theme/
license @ GPL3
src_url @ http://faenza-icon-theme.googlecode.com/files/$name_$version.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

def install():
    for item in ("Faenza",  "Faenza-Dark",  "Faenza-Darker",  "Faenza-Darkest"):
        copytree("../"+item, "/usr/share/icons/%s" % item)

    insdoc("AUTHORS", "ChangeLog", "README")
