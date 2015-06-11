metadata = """
summary @ Meta package for KDE4 desktop
homepage @ http://www.kde.org/
license @ GPL-2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kde-runtime >=kde-base/kdelibs >=kde-base/kde-workspace
x11-base/xorg-server >=kde-base/dolphin >=kde-base/plasma x11-themes/kfaenza-icon-theme
"""

standard_procedure = False

def post_install():
    notify("Don't forget to apply KFaenza icon theme in systemsettings :) ")
