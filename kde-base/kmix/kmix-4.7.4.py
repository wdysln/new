metadata = """
summary @ Sound Mixer
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kdemultimedia-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kde-runtime
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
srcdir = "kdemultimedia-%s" % version
extract = lambda: tar_extract("kdemultimedia-%s.tar.bz2" % version)
prepare   = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir+"/kmix"))
build     = lambda: (cd("build/kmix"), make())
install   = lambda: (cd("build/kmix"), installd())
post_install = lambda: xdg_icon_resource()
