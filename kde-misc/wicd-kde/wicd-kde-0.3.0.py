metadata = """
summary @ Wicd client build on the KDE Development Platform
homepage @ http://kde-apps.org/content/show.php/Wicd+Client+KDE?content=132366
license @ GPL
src_url @ http://kde-apps.org/CONTENT/content-files/132366-$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-util/automoc4
runtime @ >=kde-base/kde-workspace-4.8.0
"""

get("main/cmake_utils")

srcdir = name

def configure():
    cmake_conf("-DPYTHONBIN=python2")

