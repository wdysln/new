metadata = """
summary @ Displays window buttons (maximise, minimise, close, etc.) in a plasmoid.
homepage @ http://kde-look.org/content/show.php/KWinButton+applet+improved?content=143971
license @ GPL
src_url @ http://dl.dropbox.com/u/4514366/kwinbuttonapplet-improved-0.5.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-util/automoc4
runtime @ >=kde-base/kde-workspace-4.8.0
"""

get("main/cmake_utils")

