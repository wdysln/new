metadata = """
summary @ Meta package for XFCE desktop
homepage @ http://www.xfce.org/
license @ GPL-2
arch @ ~x86_64
"""

depends = """
build @ dev-perl/XML-Parser x11-misc/xcb-util
runtime @ >=xfce-base/xfwm4-4.9 >=xfce-extra/xfce4-appfinder-4.9 >=xfce-base/xfdesktop-4.9 >=xfce-base/xfce4-session-4.9 x11-base/xorg-server 
xfce-extra/xfce4-mixer x11-terms/xfce4-terminal xfce-base/thunar xfce-base/xfce4-settings dev-util/geany
"""

standard_procedure = False
