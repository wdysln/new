metadata = """
summary @ A unit test framework for C
homepage @ http://sourceforge.net/projects/check/
license @ LGPL-2.1
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86_64
"""

# TODO: add subunit option

def configure():
    conf("--disable-dependency-tracking")

def install():
    installd()
    insdoc("AUTHORS", "*ChangeLog*", "NEWS", "README", "THANKS", "TODO")

