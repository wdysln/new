metadata = """
summary @ Taskbar replacement Smooth-tasks with support new KDE 4.8 API's
homepage @ http://kde-look.org/content/show.php/Smooth+Tasks+2?content=148813
license @ GPL2
src_url @ http://beonis.fr/$name-v2012-02-13.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake
runtime @ >=kde-base/kde-workspace-4.8.0
"""

get("main/cmake_utils")

srcdir = "."

